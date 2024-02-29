(function($){"use strict";$(document).ready(function(){var contactForm=$('#contact-form');contactForm.on('submit',function(e){window.setTimeout(function(){var errors=$('.has-error');if(errors.length){$('html, body').animate({scrollTop:150},500);}},0);if(!e.isDefaultPrevented()){var url="includes/contact-form.html";$.ajax({type:"POST",url:url,data:$(this).serialize(),success:function(data)
{var result=JSON.parse(data);console.log(result);var messageAlert=result.type+"";var messageText=result.message+"";if(messageAlert&&messageText){swal("",messageText,messageAlert);contactForm[0].reset();}}});return false;}});});var input=$('.validate-input input, .validate-input textarea');$('.validate-form').on('submit',function(){var check=true;for(var i=0;i<input.length;i++){if(validate(input[i])===false){showValidate(input[i]);check=false;}}
return check;});$(input).each(function(){$(this).on('focus',function(){hideValidate(this);});});function validate(input){if($(input).attr('type')==='email'||$(input).attr('name')==='email'){if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/)===null){return false;}}
else{if($(input).val().trim()===''){return false;}}}
function showValidate(input){var thisAlert=$(input).parent();$(thisAlert).addClass('alert-validate');}
function hideValidate(input){var thisAlert=$(input).parent();$(thisAlert).removeClass('alert-validate');}})(jQuery);