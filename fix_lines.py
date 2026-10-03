import io

file = r'C:\Users\User\OneDrive\Desktop\Kyrgyz4x4rentals\index.html'

with io.open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

replacements = {
    1168: '                    <li data-lang="terms_g8">Breakdowns and problems as a result of the client\u2019s negligence will be charged in full to the client, including any recovery fees incurred by \u201cKyrgyz4x4rentals\u201d.</li>\n',
    1169: '                    <li data-lang="terms_g9">The client is responsible to follow all laws and regulations of the country in which they are operating the vehicle. Any legal fees incurred by \u201cKyrgyz4x4rentals\u201d as a result of the client\u2019s actions will be charged to the client.</li>\n',
    1170: '                    <li data-lang="terms_g10"><b>\u0420\u0435\u0433\u0438\u043e\u043d\u044b \u043f\u0440\u0438\u0435\u043c\u0430/\u0441\u0434\u0430\u0447\u0438:</b> \u041f\u0440\u0438\u0435\u043c \u0438 \u0432\u043e\u0437\u0432\u0440\u0430\u0442 \u043c\u0430\u0448\u0438\u043d\u044b \u0432 \u0434\u0440\u0443\u0433\u0438\u0445 \u0440\u0435\u0433\u0438\u043e\u043d\u0430\u0445 \u043f\u043e\u043c\u0438\u043c\u043e \u0411\u0438\u0448\u043a\u0435\u043a\u0430 \u043e\u0431\u0441\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e \u0441 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u043c \u043f\u0440\u0438 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0438 \u043f\u043e \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0430\u043c.</li>\n',
    1177: '                    <li data-lang="terms_b1"><b>If the client wants to return the car during the trip for his own reason</b>, the company does not return the money for the remaining days, as the order of other orders will be violated. (\u041f\u0440\u0438 \u0434\u043e\u0441\u0440\u043e\u0447\u043d\u043e\u043c \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0435 \u043f\u043e \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u043e\u043f\u043b\u0430\u0442\u0430 \u0437\u0430 \u043e\u0441\u0442\u0430\u0432\u0448\u0438\u0435\u0441\u044f \u0434\u043d\u0435\u0439 \u043d\u0435 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f).</li>\n',
    1178: '                    <li data-lang="terms_b2">Breakdowns are an unfortunate part of life in Central Asia. In the event that your vehicle breaks down, please inform \u201cKyrgyz4x4rentals\u201d immediately.</li>\n',
    1179: '                    <li data-lang="terms_b3">Inside Kyrgyzstan \u201cKyrgyz4x4rentals\u201d or its representative will repair the vehicle or supply an alternative. If no alternative options suitable to the client can be arranged, then a refund of the unused days will be made.</li>\n',
    1180: '                    <li data-lang="terms_b4">\u201cKyrgyz4x4rentals\u201d is not obligated to refund lost time due to a breakdown and will do so only at its discretion.</li>\n',
    1187: '                    <li data-lang="terms_i1"><b>Deductible (\u0414\u0435\u043f\u043e\u0437\u0438\u0442 / \u0424\u0440\u0430\u043d\u0448\u0438\u0437\u0430):</b> 800 euro.</li>\n',
    1188: '                    <li data-lang="terms_i2"><b>\u0423\u0441\u043b\u043e\u0432\u0438\u0435 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0430 \u0434\u0435\u043f\u043e\u0437\u0438\u0442\u0430:</b> \u0415\u0441\u043b\u0438 \u043f\u0440\u0438 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0435 \u043c\u0430\u0448\u0438\u043d\u044b \u043d\u0435 \u0432\u044b\u044f\u0432\u0438\u0442\u0441\u044f \u0432\u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0439 \u041f\u0414\u0414, \u0448\u0442\u0440\u0430\u0444\u043e\u0432 \u0430 \u043f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0439 \u043a\u0443\u0437\u043e\u0432\u0430/\u0438\u043d\u0442\u0435\u0440\u044c\u0435\u0440\u0430, \u0437\u0430\u043b\u043e\u0433 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0443 \u0432 \u043f\u043e\u043b\u043d\u043e\u043c \u043e\u0431\u044a\u0435\u043c\u0435 (800\u20ac) \u043f\u0440\u0438 \u0436\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0438 \u043f\u043e\u0435\u0437\u0434\u043a\u0438! \u0415\u0441\u043b\u0438 \u0432\u044b\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0432\u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u044f, \u0446\u0430\u0440\u0430\u043f\u0438\u043d\u044b \u0438\u043b\u0438 \u0448\u0442\u0440\u0430\u0444\u044b \u2014 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u0432\u044b\u0447\u0438\u0442\u0430\u0435\u0442\u0441\u044f (\u043c\u0438\u043d\u0443\u0441\u0443\u0435\u0442\u0441\u044f) \u0438\u0437 \u0434\u0435\u043f\u043e\u0437\u0438\u0442\u0430.</li>\n',
    1189: '                    <li data-lang="terms_i3">\u201cKyrgyz4x4rentals\u201d will not refund lost time due to an accident.</li>\n',
    1196: '                    <li data-lang="terms_c1">Lost Key (\u041f\u043e\u0442\u0435\u0440\u044f \u043a\u043b\u044e\u0447\u0430): 20 \u20ac (\u0431\u0435\u0437 \u0447\u0438\u043f\u0430); 100 \u20ac (\u0441 \u0447\u0438\u043f\u043e\u043c)</li>\n',
    1197: '                    <li data-lang="terms_c2">Unrepairable Tire Damage (\u041d\u0435\u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u043c\u043e\u0435 \u043f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435 \u0448\u0438\u043d\u044b): 100 \u20ac</li>\n',
    1198: '                    <li data-lang="terms_c3">Scratches to bumpers or light damage (\u0426\u0430\u0440\u0430\u043f\u0438\u043d\u044b \u0438 \u043c\u0435\u043b\u043a\u0438\u0435 \u043f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f): Typically 200 - 300 \u20ac</li>\n',
    1199: '                    <li data-lang="terms_c4">Dirty car (\u0413\u0440\u044f\u0437\u043d\u044b\u0439 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c \u043f\u0440\u0438 \u0441\u0434\u0430\u0447\u0435): 30 \u20ac</li>\n',
}

for idx, new_line in replacements.items():
    lines[idx] = new_line

with io.open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done')
