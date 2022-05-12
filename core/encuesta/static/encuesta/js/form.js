var fv;

document.addEventListener('DOMContentLoaded', function (event) {
    const form = document.getElementById('frmForm');
    const submitButton = form.querySelector('[type="submit"]');
    fv = FormValidation.formValidation(form, {
            locale: 'es_ES',
            localization: FormValidation.locales.es_ES,
            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                submitButton: new FormValidation.plugins.SubmitButton(),
                // defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
                bootstrap: new FormValidation.plugins.Bootstrap(),
                icon: new FormValidation.plugins.Icon({
                    valid: 'fa fa-check',
                    invalid: 'fa fa-times',
                    validating: 'fa fa-refresh',
                }),
            },
            fields: {
                correo: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 5,
                        },
                        regexp: {
                            regexp: /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/i,
                            message: 'El email no es correcto'
                        },
                        //digits: {},
                        remote: {
                            url: pathname,
                            data: function () {
                                return {
                                    obj: form.querySelector('[name="correo"]').value,
                                    type: 'correo',
                                    action: 'validate_data'
                                };
                            },
                            message: 'El correo ya se encuentra registrado' ,
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                        }
                    }
                },
                
                nombre: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                        
                    }
                },
                apaterno: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                        
                    }
                },
                amaterno: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                        
                    }
                },
                telefono_movil: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                        
                    }
                },
            }
        }
    )
        .on('core.element.validated', function (e) {
            if (e.valid) {
                const groupEle = FormValidation.utils.closest(e.element, '.form-group');
                if (groupEle) {
                    FormValidation.utils.classSet(groupEle, {
                        'has-success': false,
                    });
                }
                FormValidation.utils.classSet(e.element, {
                    'is-valid': false,
                });
            }
            const iconPlugin = fv.getPlugin('icon');
            const iconElement = iconPlugin && iconPlugin.icons.has(e.element) ? iconPlugin.icons.get(e.element) : null;
            iconElement && (iconElement.style.display = 'none');
        })
        .on('core.validator.validated', function (e) {
            if (!e.result.valid) {
                const messages = [].slice.call(form.querySelectorAll('[data-field="' + e.field + '"][data-validator]'));
                messages.forEach((messageEle) => {
                    const validator = messageEle.getAttribute('data-validator');
                    messageEle.style.display = validator === e.validator ? 'block' : 'none';
                });
            }
        })
        .on('core.form.valid', function () {
            submit_formdata_with_ajax_form(fv);
        });
});

$(function () {

    $('.select2').select2({
        theme: 'bootstrap4',
        language: 'es'
        
    });
    
    $('input[name="correo"]').on('keypress', function (e) {
        return validate_form_text('string', e, null);
    });

    $('input[name="telefono_movil"]').on('keypress', function (e) {
        return validate_form_text('numbers', e, null);
    });


});