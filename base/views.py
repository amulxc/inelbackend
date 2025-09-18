from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import InvestorSubheading

def investor_subheading_manager(request):
    """View to display the drag-and-drop interface for managing investor subheadings"""
    from django.middleware.csrf import get_token
    context = {
        'csrf_token': get_token(request)
    }
    return render(request, 'base/investor_subheading_manager.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def update_subheading_order(request):
    """API endpoint to update the order of investor subheadings"""
    try:
        data = json.loads(request.body)
        order_data = data.get('order_data', [])
        
        if not isinstance(order_data, list):
            return JsonResponse({"error": "order_data must be a list"}, status=400)
        
        # Update each item's order
        for item_data in order_data:
            item_id = item_data.get('id')
            new_order = item_data.get('order')
            
            if item_id is None or new_order is None:
                return JsonResponse(
                    {"error": "Each item must have 'id' and 'order' fields"}, 
                    status=400
                )
            
            try:
                subheading = InvestorSubheading.objects.get(id=item_id)
                subheading.order = new_order
                subheading.save()
            except InvestorSubheading.DoesNotExist:
                return JsonResponse(
                    {"error": f"InvestorSubheading with id {item_id} not found"}, 
                    status=404
                )
        
        return JsonResponse({"message": "Order updated successfully"})
        
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
