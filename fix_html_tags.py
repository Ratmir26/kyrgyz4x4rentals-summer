import io

file = r'C:\Users\User\OneDrive\Desktop\Kyrgyz4x4rentals\index.html'

with io.open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix innerText to innerHTML for data-lang elements
content = content.replace(
    "element.innerText = translations[currentLang][key];",
    "element.innerHTML = translations[currentLang][key];"
)

# 2. Add missing RU keys
ru_additions = {
    'forbidden_title': 'Forbidden Roads / \u0417\u0430\u043f\u0440\u0435\u0442\u043d\u044b\u0435 \u0437\u043e\u043d\u044b',
    'contact_whatsapp_btn': '\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 WhatsApp',
    'contact_telegram_btn': '\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 Telegram',
    'contact_email_label': 'Email:',
    'contact_whatsapp_label': 'WhatsApp:',
    'contact_telegram_label': 'Telegram:',
    'contact_instagram_label': 'Instagram:',
    'spec_drive': '\u041f\u043e\u043b\u043d\u044b\u0439 \u043f\u0440\u0438\u0432\u043e\u0434 (4WD)',
    'spec_transmission': '\u0410\u0432\u0442\u043e\u043c\u0430\u0442',
    'spec_color': '\u0426\u0432\u0435\u0442',
}

# Find RU section and add missing keys before modal_agree
for key, value in ru_additions.items():
    if f'{key}:' not in content:
        content = content.replace(
            '                modal_agree: "\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f"\n            },',
            '                ' + key + ': "' + value + '",\n                modal_agree: "\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f"\n            },'
        )

# 3. Fix RU translations for Terms (remove Russian from EN, keep RU correct)
ru_terms = {
    'terms_general': 'General / \u041e\u0431\u0449\u0438\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f',
    'terms_g1': 'The vehicle may not be transferred to a third party. (\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e \u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u0435\u0440\u0435\u0434\u0430\u043d\u043e \u0442\u0440\u0435\u0442\u044c\u0438\u043c \u043b\u0438\u0446\u0430\u043c).',
    'terms_g2': 'The vehicle must be returned clean. (\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0435\u043d \u0432 \u0447\u0438\u0441\u0442\u043e\u043c \u0432\u0438\u0434\u0435).',
    'terms_g3': 'The client is responsible to safely operate the vehicle:',
    'terms_g3a': 'The client must ensure that the vehicle remains in roadworthy condition.',
    'terms_g3b': 'Oil and Coolant must be checked regularly. (\u041c\u0430\u0441\u043b\u043e \u0438 \u043e\u0445\u043b\u0430\u0436\u0434\u0430\u044e\u0449\u0430\u044f \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u044c \u0434\u043e\u043b\u0436\u043d\u044b \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c\u0441\u044f \u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u043e).',
    'terms_g3c': 'Tires and tire pressure should be observed regularly. (\u0428\u0438\u043d\u044b \u0438 \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0432 \u0448\u0438\u043d\u0430\u0445 \u0434\u043e\u043b\u0436\u043d\u044b \u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u043e \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c\u0441\u044f).',
    'terms_g3d': '\u201cKyrgyz4x4rentals\u201d must be notified immediately if the vehicle has reached its service interval.',
    'terms_g3e': 'Small repairs (up to 100 USD) of a non-critical nature may be performed by the client, but will not be reimbursed without prior agreement by \u201cKyrgyz4x4rentals\u201d.',
    'terms_g3f': 'Major repairs (over 100 USD) may only be performed with \u201cKyrgyz4x4rentals\u2019\u201d approval.',
    'terms_g4': 'All road fines are the responsibility of the driver. (\u0412\u0441\u0435 \u0448\u0442\u0440\u0430\u0444\u044b \u0437\u0430 \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u044f \u041f\u0414\u0414 \u043b\u0435\u0436\u0430\u0442 \u043d\u0430 \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f).',
    'terms_g5': 'Damage resulting from negligence (i.e. use of incorrect fuel, ignoring gauges/warning lights, unjustified off roading etc.) is not covered by insurance and will be charged to the driver/client.',
    'terms_g6': 'Ignoring the instructions of any \u201cKyrgyz4x4rentals\u201d staff or representative will result in the forfeit of the security deposit.',
    'terms_g7': 'The client must keep the vehicle locked when not present with the vehicle.',
    'terms_g8': 'Breakdowns and problems as a result of the client\u2019s negligence will be charged in full to the client, including any recovery fees incurred by \u201cKyrgyz4x4rentals\u201d.',
    'terms_g9': 'The client is responsible to follow all laws and regulations of the country in which they are operating the vehicle. Any legal fees incurred by \u201cKyrgyz4x4rentals\u201d as a result of the client\u2019s actions will be charged to the client.',
    'terms_g10': '<b>\u0420\u0435\u0433\u0438\u043e\u043d\u044b \u043f\u0440\u0438\u0435\u043c\u0430/\u0441\u0434\u0430\u0447\u0438:</b> \u041f\u0440\u0438\u0435\u043c \u0438 \u0432\u043e\u0437\u0432\u0440\u0430\u0442 \u043c\u0430\u0448\u0438\u043d\u044b \u0432 \u0434\u0440\u0443\u0433\u0438\u0445 \u0440\u0435\u0433\u0438\u043e\u043d\u0430\u0445 \u043f\u043e\u043c\u0438\u043c\u043e \u0411\u0438\u0448\u043a\u0435\u043a\u0430 \u043e\u0431\u0441\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e \u0441 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u043c \u043f\u0440\u0438 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0438 \u043f\u043e \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0430\u043c.',
    'terms_breakdowns': 'Breakdowns / \u041f\u043e\u043b\u043e\u043c\u043a\u0438 \u0438 \u0414\u043e\u0441\u0440\u043e\u0447\u043d\u044b\u0439 \u0432\u043e\u0437\u0432\u0440\u0430\u0442',
    'terms_b1': '<b>If the client wants to return the car during the trip for his own reason</b>, the company does not return the money for the remaining days, as the order of other orders will be violated. (\u041f\u0440\u0438 \u0434\u043e\u0441\u0440\u043e\u0447\u043d\u043e\u043c \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0435 \u043f\u043e \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u043e\u043f\u043b\u0430\u0442\u0430 \u0437\u0430 \u043e\u0441\u0442\u0430\u0432\u0448\u0438\u0435\u0441\u044f \u0434\u043d\u0435\u0439 \u043d\u0435 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f).',
    'terms_b2': 'Breakdowns are an unfortunate part of life in Central Asia. In the event that your vehicle breaks down, please inform \u201cKyrgyz4x4rentals\u201d immediately.',
    'terms_b3': 'Inside Kyrgyzstan \u201cKyrgyz4x4rentals\u201d or its representative will repair the vehicle or supply an alternative. If no alternative options suitable to the client can be arranged, then a refund of the unused days will be made.',
    'terms_b4': '\u201cKyrgyz4x4rentals\u201d is not obligated to refund lost time due to a breakdown and will do so only at its discretion.',
    'terms_insurance': 'Insurance & Deposit Return / \u0421\u0442\u0440\u0430\u0445\u043e\u0432\u043a\u0430 \u0438 \u0412\u043e\u0437\u0432\u0440\u0430\u0442 \u0434\u0435\u043f\u043e\u0437\u0438\u0442\u0430',
    'terms_i1': '<b>Deductible (\u0414\u0435\u043f\u043e\u0437\u0438\u0442 / \u0424\u0440\u0430\u043d\u0448\u0438\u0437\u0430):</b> 800 euro.',
    'terms_i2': '<b>\u0423\u0441\u043b\u043e\u0432\u0438\u0435 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0430 \u0434\u0435\u043f\u043e\u0437\u0438\u0442\u0430:</b> \u0415\u0441\u043b\u0438 \u043f\u0440\u0438 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0435 \u043c\u0430\u0448\u0438\u043d\u044b \u043d\u0435 \u0432\u044b\u044f\u0432\u0438\u0442\u0441\u044f \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0439 \u041f\u0414\u0414, \u0448\u0442\u0440\u0430\u0444\u043e\u0432 \u0438 \u043f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0439 \u043a\u0443\u0437\u043e\u0432\u0430/\u0438\u043d\u0442\u0435\u0440\u044c\u0435\u0440\u0430, \u0437\u0430\u043b\u043e\u0433 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0443 \u0432 \u043f\u043e\u043b\u043d\u043e\u043c \u043e\u0431\u044a\u0435\u043c\u0435 (800\u20ac) \u043f\u0440\u0438 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0438 \u043f\u043e\u0435\u0437\u0434\u043a\u0438! \u0415\u0441\u043b\u0438 \u0432\u044b\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u044f, \u0446\u0430\u0440\u0430\u043f\u0438\u043d\u044b \u0438\u043b\u0438 \u0448\u0442\u0440\u0430\u0444\u044b \u2014 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u0432\u044b\u0447\u0438\u0442\u0430\u0435\u0442\u0441\u044f (\u043c\u0438\u043d\u0443\u0441\u0443\u0435\u0442\u0441\u044f) \u0438\u0437 \u0434\u0435\u043f\u043e\u0437\u0438\u0442\u0430.',
    'terms_i3': '\u201cKyrgyz4x4rentals\u201d will not refund lost time due to an accident.',
    'terms_costs': 'Standard Costs / \u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0435 \u0432\u044b\u0447\u0435\u0442\u044b (\u043f\u0440\u0438\u043c\u0435\u0440\u044b)',
    'terms_c1': 'Lost Key (\u041f\u043e\u0442\u0435\u0440\u044f \u043a\u043b\u044e\u0447\u0430): 20 \u20ac (\u0431\u0435\u0437 \u0447\u0438\u043f\u0430); 100 \u20ac (\u0441 \u0447\u0438\u043f\u043e\u043c)',
    'terms_c2': 'Unrepairable Tire Damage (\u041d\u0435\u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u043c\u043e\u0435 \u043f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435 \u0448\u0438\u043d\u044b): 100 \u20ac',
    'terms_c3': 'Scratches to bumpers or light damage (\u0426\u0430\u0440\u0430\u043f\u0438\u043d\u044b \u0438 \u043c\u0435\u043b\u043a\u0438\u0435 \u043f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f): Typically 200 - 300 \u20ac',
    'terms_c4': 'Dirty car (\u0413\u0440\u044f\u0437\u043d\u044b\u0439 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c \u043f\u0440\u0438 \u0441\u0434\u0430\u0447\u0435): 30 \u20ac',
}

# Fix RU section
ru_section_start = content.find('ru: {')
if ru_section_start != -1:
    ru_section = content[ru_section_start:]
    for key, value in ru_terms.items():
        old = f'{key}: "'
        pos = ru_section.find(old)
        if pos != -1:
            start = pos + len(old)
            end = ru_section.find('"', start)
            if end != -1:
                content = content[:ru_section_start + start] + value + content[ru_section_start + end:]

# 4. Fix EN section - remove Russian text
en_terms = {
    'terms_general': 'General Terms',
    'terms_g1': 'The vehicle may not be transferred to a third party.',
    'terms_g2': 'The vehicle must be returned clean.',
    'terms_g3': 'The client is responsible to safely operate the vehicle:',
    'terms_g3a': 'The client must ensure that the vehicle remains in roadworthy condition.',
    'terms_g3b': 'Oil and Coolant must be checked regularly.',
    'terms_g3c': 'Tires and tire pressure should be observed regularly.',
    'terms_g3d': '\u201cKyrgyz4x4rentals\u201d must be notified immediately if the vehicle has reached its service interval.',
    'terms_g3e': 'Small repairs (up to 100 USD) of a non-critical nature may be performed by the client, but will not be reimbursed without prior agreement by \u201cKyrgyz4x4rentals\u201d.',
    'terms_g3f': 'Major repairs (over 100 USD) may only be performed with \u201cKyrgyz4x4rentals\u2019\u201d approval.',
    'terms_g4': 'All road fines are the responsibility of the driver.',
    'terms_g5': 'Damage resulting from negligence (i.e. use of incorrect fuel, ignoring gauges/warning lights, unjustified off roading etc.) is not covered by insurance and will be charged to the driver/client.',
    'terms_g6': 'Ignoring the instructions of any \u201cKyrgyz4x4rentals\u201d staff or representative will result in the forfeit of the security deposit.',
    'terms_g7': 'The client must keep the vehicle locked when not present with the vehicle.',
    'terms_g8': 'Breakdowns and problems as a result of the client\u2019s negligence will be charged in full to the client, including any recovery fees incurred by \u201cKyrgyz4x4rentals\u201d.',
    'terms_g9': 'The client is responsible to follow all laws and regulations of the country in which they are operating the vehicle. Any legal fees incurred by \u201cKyrgyz4x4rentals\u201d as a result of the client\u2019s actions will be charged to the client.',
    'terms_g10': '<b>Pick-up / Return regions:</b> Pick-up and return of the vehicle in regions other than Bishkek is discussed individually with the client upon contact.',
    'terms_breakdowns': 'Breakdowns / Early Return',
    'terms_b1': '<b>If the client wants to return the car during the trip for his own reason</b>, the company does not return the money for the remaining days, as the order of other orders will be violated.',
    'terms_b2': 'Breakdowns are an unfortunate part of life in Central Asia. In the event that your vehicle breaks down, please inform \u201cKyrgyz4x4rentals\u201d immediately.',
    'terms_b3': 'Inside Kyrgyzstan \u201cKyrgyz4x4rentals\u201d or its representative will repair the vehicle or supply an alternative. If no alternative options suitable to the client can be arranged, then a refund of the unused days will be made.',
    'terms_b4': '\u201cKyrgyz4x4rentals\u201d is not obligated to refund lost time due to a breakdown and will do so only at its discretion.',
    'terms_insurance': 'Insurance & Deposit Return',
    'terms_i1': '<b>Deductible:</b> 800 euro.',
    'terms_i2': '<b>Deposit return condition:</b> If no traffic violations, fines, or body/interior damage are found upon return, the deposit is returned to the client in full (800\u20ac) upon completion of the trip! If violations, scratches, or fines are found, the corresponding amount is deducted from the deposit.',
    'terms_i3': '\u201cKyrgyz4x4rentals\u201d will not refund lost time due to an accident.',
    'terms_costs': 'Standard Costs (examples)',
    'terms_c1': 'Lost Key: 20 \u20ac (without chip); 100 \u20ac (with chip)',
    'terms_c2': 'Unrepairable Tire Damage: 100 \u20ac',
    'terms_c3': 'Scratches to bumpers or light damage: Typically 200 - 300 \u20ac',
    'terms_c4': 'Dirty car upon return: 30 \u20ac',
}

en_section_start = content.find('en: {')
if en_section_start != -1:
    en_section = content[en_section_start:]
    for key, value in en_terms.items():
        old = f'{key}: "'
        pos = en_section.find(old)
        if pos != -1:
            start = pos + len(old)
            end = en_section.find('"', start)
            if end != -1:
                content = content[:en_section_start + start] + value + content[en_section_start + end:]

with io.open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print('All fixes applied!')
