p='android/app/src/main/AndroidManifest.xml'
s=open(p,encoding='utf-8').read()
names=['ACCESS_FINE_LOCATION','ACCESS_COARSE_LOCATION','FOREGROUND_SERVICE','FOREGROUND_SERVICE_LOCATION','POST_NOTIFICATIONS','WAKE_LOCK','VIBRATE']
perms=''.join('    <uses-permission android:name="android.permission.%s" />\n'%n for n in names)
svc='        <service android:name="com.equimaps.capacitor_background_geolocation.BackgroundGeolocationService" android:enabled="true" android:exported="true" android:foregroundServiceType="location" />\n'
assert '</application>' in s and '</manifest>' in s
s=s.replace('</application>',svc+'    </application>',1)
s=s.replace('</manifest>',perms+'</manifest>',1)
open(p,'w',encoding='utf-8').write(s)
print('Manifest parcheado')

# ---------------- ICONO DE LA APP ----------------
# Pon tu imagen en la raiz del repositorio con el nombre icono.png (tambien sirve icono.jpg).
# Debe ser cuadrada y con lo importante hacia el centro. Si no hay imagen, se deja el icono de fabrica.
import os, shutil
try:
    img = None
    for f in sorted(os.listdir('.')):
        if f.lower() in ('icono.png', 'icono.jpg', 'icono.jpeg', 'icono.webp'):
            img = f
            break
    if not img:
        raise Exception('no hay icono.png en la raiz del repositorio')
    ext = '.' + img.lower().rsplit('.', 1)[1].replace('jpeg', 'jpg')
    RES = 'android/app/src/main/res'
    for d in ('mipmap-xxxhdpi', 'values', 'mipmap-anydpi-v26'):
        os.makedirs(RES + '/' + d, exist_ok=True)
    shutil.copyfile(img, RES + '/mipmap-xxxhdpi/moto_icon_fg' + ext)
    open(RES + '/values/moto_icon.xml', 'w', encoding='utf-8').write(
        '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="moto_icon_bg">#2F5A53</color>\n</resources>\n')
    ADAPT = ('<?xml version="1.0" encoding="utf-8"?>\n'
             '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
             '    <background android:drawable="@color/moto_icon_bg"/>\n'
             '    <foreground android:drawable="@mipmap/moto_icon_fg"/>\n'
             '</adaptive-icon>\n')
    for nombre in ('ic_launcher.xml', 'ic_launcher_round.xml'):
        open(RES + '/mipmap-anydpi-v26/' + nombre, 'w', encoding='utf-8').write(ADAPT)
    # pantalla de arranque: fondo liso en lugar del logo de Capacitor
    st = RES + '/values/styles.xml'
    if os.path.exists(st):
        t = open(st, encoding='utf-8').read()
        if '@drawable/splash' in t:
            open(st, 'w', encoding='utf-8').write(t.replace('@drawable/splash', '@color/moto_icon_bg'))
    print('Icono parcheado con', img)
except Exception as e:
    print('AVISO: no se pudo poner el icono nuevo, se deja el de fabrica:', e)
