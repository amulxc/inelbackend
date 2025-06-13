(function($) {
    'use strict';

    // Function to toggle CK editor visibility
    function toggleCKEditor(useEditorCheckbox) {
        var $editorField = useEditorCheckbox.closest('fieldset, .form-row, tr').find('.django-ckeditor-widget, [id*="editor_content"]').closest('.field-editor_content, .form-row, td');
        
        if (useEditorCheckbox.checked) {
            $editorField.show();
            // Initialize CK editor if not already initialized
            var textareaId = $editorField.find('textarea').attr('id');
            if (textareaId && typeof CKEDITOR !== 'undefined') {
                if (!CKEDITOR.instances[textareaId]) {
                    CKEDITOR.replace(textareaId);
                }
            }
        } else {
            $editorField.hide();
        }
    }

    // Function to handle individual form (for change form)
    function handleForm() {
        var $useEditorCheckbox = $('input[name="use_editor"], input[name*="use_editor"]');
        
        $useEditorCheckbox.each(function() {
            var checkbox = this;
            // Set initial state
            toggleCKEditor(checkbox);
            
            // Add event listener
            $(checkbox).on('change', function() {
                toggleCKEditor(checkbox);
            });
        });
    }

    // Function to handle inline formsets
    function handleInlineFormsets() {
        var $inlineGroups = $('.inline-group');
        
        $inlineGroups.each(function() {
            var $inlineGroup = $(this);
            
            // Handle existing forms
            $inlineGroup.find('.form-row, tr').each(function() {
                var $row = $(this);
                var $useEditorCheckbox = $row.find('input[name*="use_editor"]');
                
                if ($useEditorCheckbox.length) {
                    toggleCKEditor($useEditorCheckbox[0]);
                    
                    $useEditorCheckbox.on('change', function() {
                        toggleCKEditor(this);
                    });
                }
            });
            
            // Handle dynamically added forms
            $inlineGroup.on('formset:added', function(event, $row) {
                var $useEditorCheckbox = $row.find('input[name*="use_editor"]');
                
                if ($useEditorCheckbox.length) {
                    toggleCKEditor($useEditorCheckbox[0]);
                    
                    $useEditorCheckbox.on('change', function() {
                        toggleCKEditor(this);
                    });
                }
            });
        });
    }

    // Function to add custom styling for better UX
    function addCustomStyling() {
        // Add some custom CSS for better visual separation
        var style = $('<style>').text(`
            .field-use_editor {
                background-color: #f8f9fa;
                padding: 8px;
                border-radius: 4px;
                margin-bottom: 10px;
            }
            .field-use_editor label {
                font-weight: bold;
                color: #2e7d32;
            }
            .collapsed .field-editor_content {
                display: none !important;
            }
            .investor-content-toggle {
                cursor: pointer;
                user-select: none;
            }
            .inline-group .add-row {
                background-color: #4CAF50;
                color: white;
                border-radius: 4px;
                padding: 8px 16px;
                text-decoration: none;
                display: inline-block;
                margin-top: 10px;
            }
            .inline-group .add-row:hover {
                background-color: #45a049;
                color: white;
                text-decoration: none;
            }
        `);
        $('head').append(style);
    }

    // Initialize when DOM is ready
    $(document).ready(function() {
        // Add custom styling
        addCustomStyling();
        
        // Handle both regular forms and inline formsets
        handleForm();
        handleInlineFormsets();
        
        // Also handle CK editor initialization after it's loaded
        if (typeof CKEDITOR !== 'undefined') {
            CKEDITOR.on('instanceReady', function(event) {
                // Additional setup if needed
            });
        }
    });

    // Handle Django admin's dynamic inline forms
    $(document).on('DOMNodeInserted', function(e) {
        if ($(e.target).hasClass('form-row') || $(e.target).find('.form-row').length) {
            setTimeout(function() {
                handleForm();
                handleInlineFormsets();
            }, 100);
        }
    });

})(django.jQuery); 