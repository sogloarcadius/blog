
# Table of Contents
 <p><div class="lev1 toc-item"><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></div><div class="lev2 toc-item"><a href="#Processus-de-compilation-Android" data-toc-modified-id="Processus-de-compilation-Android-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Processus de compilation Android</a></div><div class="lev2 toc-item"><a href="#Ressources" data-toc-modified-id="Ressources-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Ressources</a></div><div class="lev1 toc-item"><a href="#Code-Examples" data-toc-modified-id="Code-Examples-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Code Examples</a></div>

# Introduction

Janvier 2007 : Apple sort Iphone

Nov 2007 : Open Handset Alliance : S.E mobile Open source : 35 entreprises s'unissent dont google. Actuellement 80 entreprises dans OHA.

Résultat : Android est sorti en 2007. La société Android Studio racheté par Google en 2005

- SQLITE pour les BDD R
- OPENGL pour les images 2d et 3d(videogames)


## Processus de compilation Android

Code java compilé par la JVM en bytecode (fichier .class),

Ensuite une double compilation par la machine virtuelle Dalvik pour traduire les instructions bytecode dans un langage assembleur compréhensible par le processeur pour éxécuter notre programme.
Interface utilisateur

(UI = View)

Layout = Gabarrit

Widget = Composant ( une vue qui ne peut pas englober d'autres vues)

Étapes pour construire interface utilisateur(user interface) : 

- choisir les composants ( widgets = TextView, ImageView, )
- positionnement des composants( gabarits : LinearLayout, Relative Layout, TableLayout, FrameLayout, …)
- Style des composants (couleur, polices, …)



## Ressources

fichier R.java , décrit toutes les ressources (layouts, strings, drawables, mipmaps…)

Ces ressources sont tres utilisés. il s'agit de fichier xml pour les layouts
Images

Vectorielles : PNG, JPEG, GIF

Matricielle : SVG , description sous forme de XML

Technologie 9-patch permet de rendre les images extensibles sans perdre en qualité.
Animations

dossier res/anim

# Code Examples


```bash
Calendar c = Calendar.getInstance();
SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss a");
String strDate = sdf.format(c.getTime());
TextView textView_date = (TextView) view.findViewById(R.id.feelings_date_now_id);
textView_date.setText(strDate);


packageName.contains(“com.twitter.android”) || packageName.contains(“com.facebook.katana”)
packageName.contains(“com.whatsapp”)
packageName.contains(“com.google.android.talk”)
packageName.contains(“com.google.android.gm”)
packageName.contains(“com.yahoo.mobile”)
packageName.contains(“com.android.mms”)

/*_token = token.getToken();
Log.v(MainActivity.TAG, _token);

Thread t1 = new Thread(new Runnable() {
@Override
public void run() {

SyncCredentials myCredentials = SyncCredentials.facebook(_token);
Logging in the User</font>
user = SyncUser.login(myCredentials, AUTH_URL);

String userJson = user.toJson();
Log.v(MainActivity.TAG, userJson);

runOnUiThread(new Runnable() {
@Override
public void run() {
Create a RealmConfiguration for our user</font>
SyncConfiguration config = new SyncConfiguration.Builder(user, SERVER_URL)

.initialData(new Realm.Transaction() {
@Override
public void execute(Realm realm) {
realm.createObject(SaveMood.class, 1);
}
})
.build();

This will automatically sync all changes in the background for as long as the Realm is open

realm = Realm.getInstance(config);
REALM_CONFIG_CREATED= true;'' }});
}
});

t1.start();*/ 

```
