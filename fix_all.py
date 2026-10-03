import io
import re

file = r'C:\Users\User\OneDrive\Desktop\Kyrgyz4x4rentals\index.html'

with io.open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix English translations for Terms (remove Russian text)
en_translations = {
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

for key, value in en_translations.items():
    # Replace in en section only (after "en: {" line)
    en_section_start = content.find('en: {')
    if en_section_start == -1:
        continue
    en_section = content[en_section_start:]
    old = f'{key}: "'
    pos = en_section.find(old)
    if pos == -1:
        continue
    start = pos + len(old)
    end = en_section.find('"', start)
    if end == -1:
        continue
    content = content[:en_section_start + start] + value + content[en_section_start + end:]

# 2. Add missing data-lang attributes in HTML
# terms_g3d
content = content.replace(
    '<li>\u201cKyrgyz4x4rentals\u201d must be notified immediately if the vehicle has reached its service interval.</li>',
    '<li data-lang="terms_g3d">\u201cKyrgyz4x4rentals\u201d must be notified immediately if the vehicle has reached its service interval.</li>'
)

# terms_g6
content = content.replace(
    '<li>Ignoring the instructions of any \u201cKyrgyz4x4rentals\u201d staff or representative will result in the forfeit of the security deposit.</li>',
    '<li data-lang="terms_g6">Ignoring the instructions of any \u201cKyrgyz4x4rentals\u201d staff or representative will result in the forfeit of the security deposit.</li>'
)

# Forbidden Zones header
content = content.replace(
    '<h2>Forbidden Roads / \u0417\u0430\u043f\u0440\u0435\u0442\u043d\u044b\u0435 \u0437\u043e\u043d\u044b</h2>',
    '<h2 data-lang="forbidden_title">Forbidden Roads / \u0417\u0430\u043f\u0440\u0435\u0442\u043d\u044b\u0435 \u0437\u043e\u043d\u044b</h2>'
)

# Contact buttons
content = content.replace(
    '<i class="fa-brands fa-whatsapp"></i> \u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 WhatsApp',
    '<i class="fa-brands fa-whatsapp"></i> <span data-lang="contact_whatsapp_btn">\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 WhatsApp</span>'
)
content = content.replace(
    '<i class="fa-brands fa-telegram"></i> \u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 Telegram',
    '<i class="fa-brands fa-telegram"></i> <span data-lang="contact_telegram_btn">\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 Telegram</span>'
)

# Contact labels
content = content.replace(
    '<div style="font-size:0.85rem; color:var(--text-muted);">Email:</div>',
    '<div style="font-size:0.85rem; color:var(--text-muted);" data-lang="contact_email_label">Email:</div>'
)
content = content.replace(
    '<div style="font-size:0.85rem; color:var(--text-muted);">WhatsApp:</div>',
    '<div style="font-size:0.85rem; color:var(--text-muted);" data-lang="contact_whatsapp_label">WhatsApp:</div>'
)
content = content.replace(
    '<div style="font-size:0.85rem; color:var(--text-muted);">Telegram:</div>',
    '<div style="font-size:0.85rem; color:var(--text-muted);" data-lang="contact_telegram_label">Telegram:</div>'
)
content = content.replace(
    '<div style="font-size:0.85rem; color:var(--text-muted);">Instagram:</div>',
    '<div style="font-size:0.85rem; color:var(--text-muted);" data-lang="contact_instagram_label">Instagram:</div>'
)

# 3. Add new translation keys
new_ru_keys = {
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

new_en_keys = {
    'forbidden_title': 'Forbidden Roads / \u0417\u0430\u043f\u0440\u0435\u0442\u043d\u044b\u0435 \u0437\u043e\u043d\u044b',
    'contact_whatsapp_btn': 'Write to WhatsApp',
    'contact_telegram_btn': 'Write to Telegram',
    'contact_email_label': 'Email:',
    'contact_whatsapp_label': 'WhatsApp:',
    'contact_telegram_label': 'Telegram:',
    'contact_instagram_label': 'Instagram:',
    'spec_drive': 'Full Drive (4WD)',
    'spec_transmission': 'Automatic',
    'spec_color': 'Color',
}

# Add new keys to RU section
ru_insert = ''
for k, v in new_ru_keys.items():
    ru_insert += f'                {k}: "{v}",\n'
content = content.replace(
    '                modal_agree: "\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f"\n            },',
    '                modal_agree: "\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f",\n' + ru_insert + '            },'
)

# Add new keys to EN section
en_insert = ''
for k, v in new_en_keys.items():
    en_insert += f'                {k}: "{v}",\n'
content = content.replace(
    '                modal_agree: "Agree Terms"\n            }',
    '                modal_agree: "Agree Terms",\n' + en_insert + '            }'
)

# 4. Update car cards - replace year with drive, add color and transmission
# Car 1
content = content.replace(
    '<div class="spec-item"><i class="fa-solid fa-calendar"></i> <span data-lang="spec_year">\u0413\u043e\u0434: 2005</span></div>',
    '<div class="spec-item"><i class="fa-solid fa-truck-monster"></i> <span data-lang="spec_drive">\u041f\u043e\u043b\u043d\u044b\u0439 \u043f\u0440\u0438\u0432\u043e\u0434 (4WD)</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-palette"></i> <span data-lang="spec_color">\u0426\u0432\u0435\u0442: \u0411\u0435\u043b\u044b\u0439</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-gear"></i> <span data-lang="spec_transmission">\u0410\u0432\u0442\u043e\u043c\u0430\u0442</span></div>'
)

# Car 2
content = content.replace(
    '<div class="spec-item"><i class="fa-solid fa-calendar"></i> <span data-lang="spec_year">\u0413\u043e\u0434: 2007</span></div>',
    '<div class="spec-item"><i class="fa-solid fa-truck-monster"></i> <span data-lang="spec_drive">\u041f\u043e\u043b\u043d\u044b\u0439 \u043f\u0440\u0438\u0432\u043e\u0434 (4WD)</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-palette"></i> <span data-lang="spec_color">\u0426\u0432\u0435\u0442: \u0421\u0435\u0440\u044b\u0439</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-gear"></i> <span data-lang="spec_transmission">\u0410\u0432\u0442\u043e\u043c\u0430\u0442</span></div>'
)

# Car 3
content = content.replace(
    '<div class="spec-item"><i class="fa-solid fa-calendar"></i> <span data-lang="spec_year">\u0413\u043e\u0434: 2004</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-campground"></i> <span data-lang="spec_tent">\u0421\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043f\u0430\u043b\u0430\u0442\u043a\u0430</span></div>\n                    </div>\n                    <a href="#pricing" class="btn btn-primary" style="margin-top:auto; text-align:center; justify-content:center;" data-lang="btn_book">\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c</a>\n                </div>\n            </div>\n\n            <!-- Car Card 4 -->',
    '<div class="spec-item"><i class="fa-solid fa-truck-monster"></i> <span data-lang="spec_drive">\u041f\u043e\u043b\u043d\u044b\u0439 \u043f\u0440\u0438\u0432\u043e\u0434 (4WD)</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-palette"></i> <span data-lang="spec_color">\u0426\u0432\u0435\u0442: \u0427\u0435\u0440\u043d\u044b\u0439</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-gear"></i> <span data-lang="spec_transmission">\u0410\u0432\u0442\u043e\u043c\u0430\u0442</span></div>\n                    </div>\n                    <a href="#pricing" class="btn btn-primary" style="margin-top:auto; text-align:center; justify-content:center;" data-lang="btn_book">\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c</a>\n                </div>\n            </div>\n\n            <!-- Car Card 4 -->'
)

# Car 4
content = content.replace(
    '<div class="spec-item"><i class="fa-solid fa-calendar"></i> <span data-lang="spec_year">\u0413\u043e\u0434: 2006</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-campground"></i> <span data-lang="spec_tent">\u0421\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043f\u0430\u043b\u0430\u0442\u043a\u0430</span></div>\n                    </div>\n                    <a href="#pricing" class="btn btn-primary" style="margin-top:auto; text-align:center; justify-content:center;" data-lang="btn_book">\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c</a>\n                </div>\n            </div>\n\n            <!-- Car Card 5: Lexus GX 470 -->',
    '<div class="spec-item"><i class="fa-solid fa-truck-monster"></i> <span data-lang="spec_drive">\u041f\u043e\u043b\u043d\u044b\u0439 \u043f\u0440\u0438\u0432\u043e\u0434 (4WD)</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-palette"></i> <span data-lang="spec_color">\u0426\u0432\u0435\u0442: \u0411\u0435\u043b\u044b\u0439</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-gear"></i> <span data-lang="spec_transmission">\u0410\u0432\u0442\u043e\u043c\u0430\u0442</span></div>\n                    </div>\n                    <a href="#pricing" class="btn btn-primary" style="margin-top:auto; text-align:center; justify-content:center;" data-lang="btn_book">\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c</a>\n                </div>\n            </div>\n\n            <!-- Car Card 5: Lexus GX 470 -->'
)

# Car 5
content = content.replace(
    '<div class="spec-item"><i class="fa-solid fa-calendar"></i> <span data-lang="spec_year">\u0413\u043e\u0434: 2004</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-campground"></i> <span data-lang="spec_tent">\u0421\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043f\u0430\u043b\u0430\u0442\u043a\u0430</span></div>\n                    </div>\n                    <a href="#pricing" class="btn btn-primary" style="margin-top:auto; text-align:center; justify-content:center;" data-lang="btn_book">\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c</a>\n                </div>\n            </div>\n        </div>\n    </section>',
    '<div class="spec-item"><i class="fa-solid fa-truck-monster"></i> <span data-lang="spec_drive">\u041f\u043e\u043b\u043d\u044b\u0439 \u043f\u0440\u0438\u0432\u043e\u0434 (4WD)</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-palette"></i> <span data-lang="spec_color">\u0426\u0432\u0435\u0442: \u0421\u0435\u0440\u044b\u0439</span></div>\n                        <div class="spec-item"><i class="fa-solid fa-gear"></i> <span data-lang="spec_transmission">\u0410\u0432\u0442\u043e\u043c\u0430\u0442</span></div>\n                    </div>\n                    <a href="#pricing" class="btn btn-primary" style="margin-top:auto; text-align:center; justify-content:center;" data-lang="btn_book">\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c</a>\n                </div>\n            </div>\n        </div>\n    </section>'
)

# 5. Fix WhatsApp message to be bilingual
content = content.replace(
    "const message = `\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435! \u0425\u043e\u0447\u0443 \u0437\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u043d\u0435\u0434\u043e\u0440\u043e\u0436\u043d\u0438\u043a \u0432 Kyrgyz4x4rentals:%0A` +\n                            `- \u041c\u0430\u0448\u0438\u043d\u0430: ${encodeURIComponent(data.car)}%0A` +\n                            `- \u0414\u043d\u0435\u0439: ${data.days}%0A` +\n                            `- \u041f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u043e\u0432: ${data.travelers}%0A` +\n                            `- \u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0443\u043c\u043c\u0430: ${data.total}\u20ac (+800\u20ac \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u043d\u044b\u0439 \u0434\u0435\u043f\u043e\u0437\u0438\u0442)`;",
    "const message = `Hello! I want to book an off-road vehicle at Kyrgyz4x4rentals:%0A` +\n                            `- Vehicle: ${encodeURIComponent(data.car)}%0A` +\n                            `- Days: ${data.days}%0A` +\n                            `- Travelers: ${data.travelers}%0A` +\n                            `- Total: ${data.total}\u20ac (+800\u20ac refundable deposit)`;"
)

with io.open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print('All fixes applied successfully!')
