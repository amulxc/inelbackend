# Investor Subheading Manager

This document explains the new drag-and-drop interface for managing InvestorSubheading data.

## Features

### 1. Model Changes
- Added `order` field to `InvestorSubheading` model
- Default ordering by the `order` field
- Migration created and applied

### 2. API Endpoints

#### Get All Investor Subheadings (Ordered)
```
GET /api/investor-subheadings/
```
Returns all investor subheadings ordered by the `order` field.

#### Update Order
```
POST /api/investor-subheadings/update_order/
```
Updates the order of multiple subheadings.

**Request Body:**
```json
{
    "order_data": [
        {"id": 1, "order": 0},
        {"id": 2, "order": 1},
        {"id": 3, "order": 2}
    ]
}
```

#### Alternative Update Order Endpoint
```
POST /api/update-subheading-order/
```
Same functionality as above, but as a standalone endpoint.

### 3. Web Interface

#### Access the Manager
Visit: `http://localhost:8000/investor-manager/`

#### Features:
- **Drag and Drop**: Reorder subheadings by dragging them
- **Visual Feedback**: Hover effects and smooth animations
- **Order Numbers**: See current position of each item
- **Save Changes**: Persist the new order to the database
- **Reset**: Revert to original order
- **Statistics**: View total count and changes made
- **Responsive Design**: Works on desktop and mobile

#### How to Use:
1. Navigate to `/investor-manager/`
2. Drag and drop items to reorder them
3. Click "Save Order" to persist changes
4. Use "Reset" to revert to original order

## Technical Details

### Database Changes
- Added `order` field (IntegerField) to `InvestorSubheading` model
- Default value: 0
- Meta ordering: `['order']`

### API Response Structure
The API maintains the same response structure as before, with the addition of the `order` field:

```json
{
    "id": 1,
    "name": "Subheading Name",
    "order": 0,
    "tab_heading": {
        "id": 1,
        "name": "Tab Heading Name"
    },
    "contents": [...]
}
```

### Frontend Technologies
- **SortableJS**: For drag and drop functionality
- **Vanilla JavaScript**: No additional frameworks
- **CSS3**: Modern styling with gradients and animations
- **Responsive Design**: Mobile-friendly interface

## Security
- CSRF protection enabled
- Input validation on all endpoints
- Error handling for invalid data

## Browser Support
- Modern browsers with ES6 support
- Drag and drop API support
- CSS Grid and Flexbox support

## Usage Examples

### Get Ordered Subheadings
```javascript
fetch('/api/investor-subheadings/')
    .then(response => response.json())
    .then(data => console.log(data));
```

### Update Order
```javascript
const orderData = [
    {id: 1, order: 0},
    {id: 2, order: 1},
    {id: 3, order: 2}
];

fetch('/api/investor-subheadings/update_order/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({order_data: orderData})
})
.then(response => response.json())
.then(data => console.log(data));
```

## Troubleshooting

### Common Issues:
1. **Migration not applied**: Run `python manage.py migrate`
2. **CSRF errors**: Ensure CSRF token is included in requests
3. **Order not saving**: Check that all items have valid IDs and order values
4. **Page not loading**: Verify the URL pattern is correctly configured

### Debug Mode:
- Check browser console for JavaScript errors
- Verify API endpoints are accessible
- Ensure database has investor subheading data
