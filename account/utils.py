from django.core.mail import send_mail


def send_activation_email(email, activation_code, is_password):
    activation_url = f'http://localhost:8000/account/activate/{activation_code}'
    if not is_password:
        message = f'''
        activate your account here {activation_url}.
        '''
        html_message = f'''
        activate your account here <a href="{activation_url}">{activation_url}</a>.
        '''
    else:
        message = f"""
        To reset your password click here {activation_url}
        """
        html_message = f"""
                To reset your password click here<a href="{activation_url}">{activation_url}</a>.
                """
    send_mail('StackOverflow Activation', message, 'admin@admin.com', [email, ], html_message=html_message,)
