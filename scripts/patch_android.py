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
