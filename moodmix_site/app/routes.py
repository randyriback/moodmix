from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms import UploadMood, UserLoginForm, UserSigninForm, ChangeGenre, ChangeMood, UploadMood
from werkzeug.utils import secure_filename
import config
import requests
import json
from flask_login import login_user, logout_user, current_user, login_required
import base64

mm = Blueprint('mm', __name__, template_folder = 'app_templates')



@mm.route('/secret', methods = ['GET', 'POST'])
@login_required
def secret():
    emotions = []
    new = User.query.get(current_user.id)
    j = new.img_token
    response = requests.post('https://api-us.faceplusplus.com/facepp/v3/face/analyze', data = { "api_key": "mKTQtUUGtQ_HC3bwVv-dcIPNAmhnt5Kl", "api_secret": config.secret, "face_tokens": j, "return_attributes": "emotion"})
    jj = json.loads(response.content)

    k = jj["faces"][0]["attributes"]["emotion"]
    return render_template("secret.html", k=k)




@mm.route('/snap')
@login_required
def snap():
    return render_template("snap.html")



@mm.route('/upload', methods = ['GET', 'POST'])
@login_required
def upload():
    x = ""
    upload_mood_form = UploadMood()
    
    try:
        if request.method == 'POST' and upload_mood_form.validate_on_submit():
            print("/////////uuuuuuuu///////")
            up = User.query.get(current_user.id)
            pic_plz = request.files['pic']
            up.img = pic_plz.read()
            db.session.commit()

            if True:
                b64 = [base64.b64encode(current_user.img).decode('ascii')]
                response = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', data = { "api_key": "mKTQtUUGtQ_HC3bwVv-dcIPNAmhnt5Kl", "api_secret": config.secret, "image_base64": b64})
                x = json.loads(response.content)
                up.img_token = x['faces'][0]['face_token']
                db.session.commit()
                return redirect(url_for('mm.new_data'))
                print(current_user.img_token)




    except:
        raise Exception("Invalid form data, please check again")

    return render_template("upload.html", upload_mood_form = upload_mood_form, x = x)

@mm.route('/new_data', methods = ['GET', 'POST'])
@login_required
def new_data():
    emotions = []
    #0 = sadness 1 = neutral 2 = disgust 3 = anger 4 = surprise5 = fear6 = happiness
    new = User.query.get(current_user.id)
    j = new.img_token
    print(j)
    response = requests.post('https://api-us.faceplusplus.com/facepp/v3/face/analyze', data = { "api_key": "mKTQtUUGtQ_HC3bwVv-dcIPNAmhnt5Kl", "api_secret": config.secret, "face_tokens": j, "return_attributes": "emotion"})
    jj = json.loads(response.content)

    for vibe in jj["faces"][0]["attributes"]["emotion"].values():
        emotions.append(vibe)
    print(max(emotions))
    print(jj["faces"][0]["attributes"]["emotion"])
    k = jj["faces"][0]["attributes"]["emotion"]

    make_mood = User.query.get(current_user.id)


    if current_user.genre == 'Ambient/Dub/Fourth World' and max(emotions) == emotions[6]: #happy
        make_mood.mood = "Morning Coffee"
        db.session.commit()
        return redirect(url_for('mm.amb'))
    elif current_user.genre == 'Ambient/Dub/Fourth World' and max(emotions) == emotions[1]: #neutral
        make_mood.mood = "Afternoon Walk"
        db.session.commit()
        return redirect(url_for('mm.amb'))  
    elif current_user.genre == 'Ambient/Dub/Fourth World' and max(emotions) == emotions[2]: #disgust
        make_mood.mood = "Reading the News"
        db.session.commit()
        return redirect(url_for('mm.amb'))
    elif current_user.genre == 'Ambient/Dub/Fourth World' and max(emotions) == emotions[3]: #anger
        make_mood.mood = "Driving in a Hurry"
        db.session.commit()
        return redirect(url_for('mm.amb'))     
    elif current_user.genre == 'Ambient/Dub/Fourth World' and max(emotions) == emotions[4]: #surprise
        make_mood.mood = "Dinner with Friends"
        db.session.commit()
        return redirect(url_for('mm.amb'))     
    elif current_user.genre == 'Ambient/Dub/Fourth World' and max(emotions) == emotions[5]: #fear
        make_mood.mood = "Late Night"
        db.session.commit()
        return redirect(url_for('mm.amb'))     
    elif current_user.genre == 'Ambient/Dub/Fourth World' and max(emotions) == emotions[0]: #sadness
        make_mood.mood = "Contemplative"
        db.session.commit()
        return redirect(url_for('mm.amb')) 

    
    
    
    if current_user.genre == 'House/Techno/Jungle/Drum n Bass' and max(emotions) == emotions[6]: #happy
        make_mood.mood = "Morning Coffee"
        db.session.commit()
        return redirect(url_for('mm.club'))
    elif current_user.genre == 'House/Techno/Jungle/Drum n Bass' and max(emotions) == emotions[1]: #neutral
        make_mood.mood = "Afternoon Walk"
        db.session.commit()
        return redirect(url_for('mm.club'))  
    elif current_user.genre == 'House/Techno/Jungle/Drum n Bass' and max(emotions) == emotions[2]: #disgust
        make_mood.mood = "Reading the News"
        db.session.commit()
        return redirect(url_for('mm.club'))
    elif current_user.genre == 'House/Techno/Jungle/Drum n Bass' and max(emotions) == emotions[3]: #anger
        make_mood.mood = "Driving in a Hurry"
        db.session.commit()
        return redirect(url_for('mm.club'))     
    elif current_user.genre == 'House/Techno/Jungle/Drum n Bass' and max(emotions) == emotions[4]: #surprise
        make_mood.mood = "Dinner with Friends"
        db.session.commit()
        return redirect(url_for('mm.club'))     
    elif current_user.genre == 'House/Techno/Jungle/Drum n Bass' and max(emotions) == emotions[5]: #fear
        make_mood.mood = "Late Night"
        db.session.commit()
        return redirect(url_for('mm.club'))     
    elif current_user.genre == 'House/Techno/Jungle/Drum n Bass' and max(emotions) == emotions[0]: #sadness
        make_mood.mood = "Contemplative"
        db.session.commit()
        return redirect(url_for('mm.club'))    

    
    
    if current_user.genre == 'Jazz/World/Soundtrack' and max(emotions) == emotions[6]: #happy
        make_mood.mood = "Morning Coffee"
        db.session.commit()
        return redirect(url_for('mm.jazz'))
    elif current_user.genre == 'Jazz/World/Soundtrack' and max(emotions) == emotions[1]: #neutral
        make_mood.mood = "Afternoon Walk"
        db.session.commit()
        return redirect(url_for('mm.jazz'))  
    elif current_user.genre == 'Jazz/World/Soundtrack' and max(emotions) == emotions[2]: #disgust
        make_mood.mood = "Reading the News"
        db.session.commit()
        return redirect(url_for('mm.jazz'))
    elif current_user.genre == 'Jazz/World/Soundtrack' and max(emotions) == emotions[3]: #anger
        make_mood.mood = "Driving in a Hurry"
        db.session.commit()
        return redirect(url_for('mm.jazz'))     
    elif current_user.genre == 'Jazz/World/Soundtrack' and max(emotions) == emotions[4]: #surprise
        make_mood.mood = "Dinner with Friends"
        db.session.commit()
        return redirect(url_for('mm.jazz'))     
    elif current_user.genre == 'Jazz/World/Soundtrack' and max(emotions) == emotions[5]: #fear
        make_mood.mood = "Late Night"
        db.session.commit()
        return redirect(url_for('mm.jazz'))     
    elif current_user.genre == 'Jazz/World/Soundtrack' and max(emotions) == emotions[0]: #sadness
        make_mood.mood = "Contemplative"
        db.session.commit()
        return redirect(url_for('mm.jazz'))


    if current_user.genre == 'Rock/Pop/Folk' and max(emotions) == emotions[6]: #happy
        make_mood.mood = "Morning Coffee"
        db.session.commit()
        return redirect(url_for('mm.pop'))
    elif current_user.genre == 'Rock/Pop/Folk' and max(emotions) == emotions[1]: #neutral
        make_mood.mood = "Afternoon Walk"
        db.session.commit()
        return redirect(url_for('mm.pop'))  
    elif current_user.genre == 'Rock/Pop/Folk' and max(emotions) == emotions[2]: #disgust
        make_mood.mood = "Reading the News"
        db.session.commit()
        return redirect(url_for('mm.pop'))
    elif current_user.genre == 'Rock/Pop/Folk' and max(emotions) == emotions[3]: #anger
        make_mood.mood = "Driving in a Hurry"
        db.session.commit()
        return redirect(url_for('mm.pop'))     
    elif current_user.genre == 'Rock/Pop/Folk' and max(emotions) == emotions[4]: #surprise
        make_mood.mood = "Dinner with Friends"
        db.session.commit()
        return redirect(url_for('mm.pop'))     
    elif current_user.genre == 'Rock/Pop/Folk' and max(emotions) == emotions[5]: #fear
        make_mood.mood = "Late Night"
        db.session.commit()
        return redirect(url_for('mm.pop'))     
    elif current_user.genre == 'Rock/Pop/Folk' and max(emotions) == emotions[0]: #sadness
        make_mood.mood = "Contemplative"
        db.session.commit()
        return redirect(url_for('mm.pop')) 


    if current_user.genre == 'Metal/Noise/Experimental' and max(emotions) == emotions[6]: #happy
        make_mood.mood = "Morning Coffee"
        db.session.commit()
        return redirect(url_for('mm.metal'))
    elif current_user.genre == 'Metal/Noise/Experimental' and max(emotions) == emotions[1]: #neutral
        make_mood.mood = "Afternoon Walk"
        db.session.commit()
        return redirect(url_for('mm.metal'))  
    elif current_user.genre == 'Metal/Noise/Experimental' and max(emotions) == emotions[2]: #disgust
        make_mood.mood = "Reading the News"
        db.session.commit()
        return redirect(url_for('mm.metal'))
    elif current_user.genre == 'Metal/Noise/Experimental' and max(emotions) == emotions[3]: #anger
        make_mood.mood = "Driving in a Hurry"
        db.session.commit()
        return redirect(url_for('mm.metal'))     
    elif current_user.genre == 'Metal/Noise/Experimental' and max(emotions) == emotions[4]: #surprise
        make_mood.mood = "Dinner with Friends"
        db.session.commit()
        return redirect(url_for('mm.metal'))     
    elif current_user.genre == 'Metal/Noise/Experimental' and max(emotions) == emotions[5]: #fear
        make_mood.mood = "Late Night"
        db.session.commit()
        return redirect(url_for('mm.metal'))     
    elif current_user.genre == 'Metal/Noise/Experimental' and max(emotions) == emotions[0]: #sadness
        make_mood.mood = "Contemplative"
        db.session.commit()
        return redirect(url_for('mm.metal'))    
                  



    return render_template("new_data.html", jj = jj, k = k)

        
    

@mm.route('/', methods = ['GET', 'POST'])
def home():
    form = UserLoginForm()
    
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            genre = request.form['genre']
            mood = request.form['mood']
            pic = request.files['pic']
            

            if genre == "Stations" or mood == "Default Mood (You Can Change Later)":
                flash('Please fill out all fields', 'user-createdy')
            
            else:
                user = User(email, genre, mood, pic.read(), img_token = "", password = password)
                login_user(user)

                db.session.add(user)
                db.session.commit()

                flash(f'Hey, {email}! Thanks for registering :)', 'user-created')

                if mood == "Facial Recognition Mode":
                    return redirect(url_for('mm.snap'))

                elif genre == "Ambient/Dub/Fourth World" and mood != "Default Mood (You Can Change Later)":
                    return redirect(url_for('mm.amb'))
                
                elif genre == "House/Techno/Jungle/Drum n Bass" and mood != "Default Mood (You Can Change Later)":
                    return redirect(url_for('mm.club'))

                elif genre == "Jazz/World/Soundtrack" and mood != "Default Mood (You Can Change Later)":
                    return redirect(url_for('mm.jazz'))
                
                elif genre == "Rock/Pop/Folk" and mood != "Default Mood (You Can Change Later)":
                    return redirect(url_for('mm.pop'))
                
                elif genre == "Metal/Noise/Experimental" and mood != "Default Mood (You Can Change Later)":
                    return redirect(url_for('mm.metal'))

                
    except:
        raise Exception("Invalid form data, please check again")
    
    return render_template("index.html", form=form)




@mm.route('/club', methods = ['GET', 'POST'])
@login_required
def club():
    club_genre_form = ChangeGenre()
    if request.method == 'POST' and club_genre_form.validate_on_submit():
        gen = User.query.get(current_user.id)
        gen_plz = request.form['genre']
        gen.genre = gen_plz
        db.session.commit()

        flash('Your default genre has been updated!', 'iuser-created')

        if gen_plz == 'Ambient/Dub/Fourth World':
            return redirect(url_for('mm.amb'))
        elif gen_plz == 'Jazz/World/Soundtrack':
            return redirect(url_for('mm.jazz'))
        elif gen_plz == 'Rock/Pop/Folk':
            return redirect(url_for('mm.pop'))
        elif gen_plz == 'Metal/Noise/Experimental':
            return redirect(url_for('mm.metal'))


    club_mood_form = ChangeMood()
    if request.method == 'POST' and club_mood_form.validate_on_submit():
        moo = User.query.get(current_user.id)
        moo_plz = request.form['mood']
        moo.mood = moo_plz
        db.session.commit()
        flash('Your mood has been updated!', 'euser-created')
    
 
    club1 = ['algo_rhythm', 'ck-safe-radio-s03e09']
    club2 = ['NTSRadio', 'andrew-weatherall-30th-janaury-2020']
    club3 = ['CrackMagazine', 'incienso-5-beta-librae']
    club4 = ['jamieryanainslie', 'bbc-radio-1-in-the-jungle-roni-size-dj-mix-01_08_97']
    club5 = ['BCR_Radio', 'west-mineral-special-with-pendant-exael-and-special-guest-dj']
    club6 = ['residentadvisor', 'ra667']
    club7 = ['NTSRadio', 'miss-modular-w-akua-28th-march-2019']

    greeting = "House/Techno/Jungle/Drum n Bass"
    greeting2 = current_user.mood
    artist = []
    song = []
    

    if current_user.mood == 'Morning Coffee':
        artist = club1[0]
        song = club1[1]
    elif current_user.mood == 'Afternoon Walk':
        artist = club2[0]
        song = club2[1]
    elif current_user.mood == 'Dinner with Friends':
        artist = club3[0]
        song = club3[1]
    elif current_user.mood == 'Late Night':
        artist = club4[0]
        song = club4[1]
    elif current_user.mood == 'Contemplative':
        artist = club5[0]
        song = club5[1]
    elif current_user.mood == 'Reading the News':
        artist = club6[0]
        song = club6[1]
    elif current_user.mood == 'Driving in a Hurry':
        artist = club7[0]
        song = club7[1]
    elif current_user.mood == 'Facial Recognition Mode':
        return redirect(url_for('mm.snap'))


    req = requests.get(f"https://www.mixcloud.com/oembed/?url=https%3A%2F%2Fwww.mixcloud.com%2F{artist}%2F{song}%2F&format=json")
    var1 = json.loads(req.content)
    new = var1['html'] 

    return render_template("club.html", new = new, greeting = greeting, greeting2 = greeting2, club_genre_form = club_genre_form, club_mood_form = club_mood_form)





@mm.route('/amb', methods = ['GET', 'POST'])
@login_required
def amb():
    amb_genre_form = ChangeGenre()
    if request.method == 'POST' and amb_genre_form.validate_on_submit():
        amby = User.query.get(current_user.id)
        amb_plz = request.form['genre']
        amby.genre = amb_plz
        db.session.commit()

        flash('Your default genre has been updated!', 'iuser-created')

        if amb_plz == 'House/Techno/Jungle/Drum n Bass':
            return redirect(url_for('mm.club'))
        elif amb_plz == 'Jazz/World/Soundtrack':
            return redirect(url_for('mm.jazz'))
        elif amb_plz == 'Rock/Pop/Folk':
            return redirect(url_for('mm.pop'))
        elif amb_plz == 'Metal/Noise/Experimental':
            return redirect(url_for('mm.metal'))

    amb_mood_form = ChangeMood()
    if request.method == 'POST' and amb_mood_form.validate_on_submit():
        amby_m = User.query.get(current_user.id)
        amby_m_plz = request.form['mood']
        amby_m.mood = amby_m_plz
        db.session.commit()
        flash('Your mood has been updated!', 'euser-created')



    amb1 = ['NTSRadio', 'sounds-of-the-dawn-10th-october-2020']
    amb2 = ['BCR_Radio', 'perila-with-pontiac-sterator']
    amb3 = ['dublab', 'matthew-mcdermott-wguest-js-motion-ward-interior-space-091120']
    amb4 = ['NTSRadio', 'in-focus-jon-hassell-29th-june-2021']
    amb5 = ['spools-out-radio', 'spools-out-radio-97-lillerne-tapes']
    amb6 = ['thelotradio', 'sweat-equity-dekalb-works-takeover-w-purelink-b2b-jung-dj-the-lot-radio-01-13-2021/']
    amb7 = ['NTSRadio', 'alien-jams-14th-may-2019']

    greeting = "Ambient/Dub/Fourth World"
    greeting2 = current_user.mood
    artist = []
    song = []

    if current_user.mood == 'Morning Coffee':
        artist = amb1[0]
        song = amb1[1]
    elif current_user.mood == 'Afternoon Walk':
        artist = amb2[0]
        song = amb2[1]
    elif current_user.mood == 'Dinner with Friends':
        artist = amb3[0]
        song = amb3[1]
    elif current_user.mood == 'Late Night':
        artist = amb4[0]
        song = amb4[1]
    elif current_user.mood == 'Contemplative':
        artist = amb5[0]
        song = amb5[1]
    elif current_user.mood == 'Reading the News':
        artist = amb6[0]
        song = amb6[1]
    elif current_user.mood == 'Driving in a Hurry':
        artist = amb7[0]
        song = amb7[1] 
    elif current_user.mood == 'Facial Recognition Mode':
        return redirect(url_for('mm.snap'))   


    req = requests.get(f"https://www.mixcloud.com/oembed/?url=https%3A%2F%2Fwww.mixcloud.com%2F{artist}%2F{song}%2F&format=json")
    var1 = json.loads(req.content)
    new = var1['html']

    change = new.replace('120', '400')

    return render_template("amb.html", change_allyse = change, new = new, greeting = greeting, greeting2 = greeting2, amb_genre_form = amb_genre_form, amb_mood_form = amb_mood_form)


@mm.route('/jazz', methods = ['GET', 'POST'])
@login_required
def jazz():
    jazz_genre_form = ChangeGenre()
    if request.method == 'POST' and jazz_genre_form.validate_on_submit():
        jazzy = User.query.get(current_user.id)
        jazz_plz = request.form['genre']
        jazzy.genre = jazz_plz
        db.session.commit()

        flash('Your default genre has been updated!', 'iuser-created')

        if jazz_plz == 'House/Techno/Jungle/Drum n Bass':
            return redirect(url_for('mm.club'))
        elif jazz_plz == 'Ambient/Dub/Fourth World':
            return redirect(url_for('mm.amb'))
        elif jazz_plz == 'Rock/Pop/Folk':
            return redirect(url_for('mm.pop'))
        elif jazz_plz == 'Metal/Noise/Experimental':
            return redirect(url_for('mm.metal'))

    jazz_mood_form = ChangeMood()
    if request.method == 'POST' and jazz_mood_form.validate_on_submit():
        jazzy_m = User.query.get(current_user.id)
        jazzy_m_plz = request.form['mood']
        jazzy_m.mood = jazzy_m_plz
        db.session.commit()
        flash('Your mood has been updated!', 'euser-created')

    jazz3 = ['NTSRadio','the-spaces-in-between-w-john-gomez-10th-march-2021']
    jazz2 = ['NTSRadio', 'cult-cargo-25th-august-2017']
    jazz1 = ['NTSRadio', 'arp-presents-the-floating-world-7th-june-2016']
    jazz4 = ['ElectronicBunker', 'mr-scruff-floating-points-dj-set-from-hare-hounds-sat-15-march-2014']
    jazz5 = ['barryandy', 'chillout-7-jazz-miles-davis-john-coltrane-billie-holiday-sarah-vaughan-nina-simone']
    jazz6 = ['Axel_de_Pontbriand', 'botanist-reggae-roots']
    jazz7 = ['NTSRadio', 'black-classical-history-of-spiritual-jazz-part-1']

    greeting = "Jazz/World/Soundtrack"
    greeting2 = current_user.mood
    artist = []
    song = []

    if current_user.mood == 'Morning Coffee':
        artist = jazz1[0]
        song = jazz1[1]
    elif current_user.mood == 'Afternoon Walk':
        artist = jazz2[0]
        song = jazz2[1]
    elif current_user.mood == 'Dinner with Friends':
        artist = jazz3[0]
        song = jazz3[1]
    elif current_user.mood == 'Late Night':
        artist = jazz4[0]
        song = jazz4[1]
    elif current_user.mood == 'Contemplative':
        artist = jazz5[0]
        song = jazz5[1]
    elif current_user.mood == 'Reading the News':
        artist = jazz6[0]
        song = jazz6[1]
    elif current_user.mood == 'Driving in a Hurry':
        artist = jazz7[0]
        song = jazz7[1]
    elif current_user.mood == 'Facial Recognition Mode':
        return redirect(url_for('mm.snap'))


    req = requests.get(f"https://www.mixcloud.com/oembed/?url=https%3A%2F%2Fwww.mixcloud.com%2F{artist}%2F{song}%2F&format=json")
    var1 = json.loads(req.content)
    new = var1['html']

    return render_template("jazz.html", new = new, greeting = greeting, greeting2 = greeting2, jazz_genre_form = jazz_genre_form, jazz_mood_form = jazz_mood_form)



@mm.route('/pop', methods = ['GET', 'POST'])
@login_required
def pop():
    pop_genre_form = ChangeGenre()
    if request.method == 'POST' and pop_genre_form.validate_on_submit():
        poppy = User.query.get(current_user.id)
        pop_plz = request.form['genre']
        poppy.genre = pop_plz
        db.session.commit()

        flash('Your default genre has been updated!', 'iuser-created')

        if pop_plz == 'House/Techno/Jungle/Drum n Bass':
            return redirect(url_for('mm.club'))
        elif pop_plz == 'Jazz/World/Soundtrack':
            return redirect(url_for('mm.jazz'))
        elif pop_plz == 'Ambient/Dub/Fourth World':
            return redirect(url_for('mm.amb'))
        elif pop_plz == 'Metal/Noise/Experimental':
            return redirect(url_for('mm.metal'))


    pop_mood_form = ChangeMood()
    if request.method == 'POST' and pop_mood_form.validate_on_submit():
        poppy_m = User.query.get(current_user.id)
        poppy_m_plz = request.form['mood']
        poppy_m.mood = poppy_m_plz
        db.session.commit()
        flash('Your mood has been updated!', 'euser-created')

    pop2 = ['okini','ladies-by-suzanne-kraft']
    pop1 = ['TimeisAway', 'mix-for-marie']
    pop3 = ['thelotradio', 'part-time-punk-the-lot-radio-05-29-2019']
    pop4 = ['dublab', 'bianca-lexis-wguest-creme-happy-hour-102516']
    pop5 = ['MurphysHorizon', 'rip-lil-peep-mix']
    pop6 = ['EncoreAmsterdam', 'mixshow-328-astroworld-day-special-by-mathiéux']
    pop7 = ['DJDayDay-1', 'djdayday_-the-best-of-pop-smoke-tribute-mix']
    
    greeting = "Rock/Pop/Folk"
    greeting2 = current_user.mood
    artist = []
    song = []

    if current_user.mood == 'Morning Coffee':
        artist = pop1[0]
        song = pop1[1]
    elif current_user.mood == 'Afternoon Walk':
        artist = pop2[0]
        song = pop2[1]
    elif current_user.mood == 'Dinner with Friends':
        artist = pop3[0]
        song = pop3[1]
    elif current_user.mood == 'Late Night':
        artist = pop4[0]
        song = pop4[1]
    elif current_user.mood == 'Contemplative':
        artist = pop5[0]
        song = pop5[1]
    elif current_user.mood == 'Reading the News':
        artist = pop6[0]
        song = pop6[1]
    elif current_user.mood == 'Driving in a Hurry':
        artist = pop7[0]
        song = pop7[1]
    elif current_user.mood == 'Facial Recognition Mode':
        return redirect(url_for('mm.snap'))


    req = requests.get(f"https://www.mixcloud.com/oembed/?url=https%3A%2F%2Fwww.mixcloud.com%2F{artist}%2F{song}%2F&format=json")
    var1 = json.loads(req.content)
    new = var1['html']
    
    
    
    return render_template("pop.html", new = new, greeting = greeting, greeting2 = greeting2, pop_genre_form = pop_genre_form, pop_mood_form = pop_mood_form)


@mm.route('/metal', methods = ['GET', 'POST'])
@login_required
def metal():
    metal_genre_form = ChangeGenre()
    if request.method == 'POST' and metal_genre_form.validate_on_submit():
        metty = User.query.get(current_user.id)
        met_plz = request.form['genre']
        metty.genre = met_plz
        db.session.commit()

        flash('Your default genre has been updated!', 'iuser-created')

        if met_plz == 'House/Techno/Jungle/Drum n Bass':
            return redirect(url_for('mm.club'))
        elif met_plz == 'Jazz/World/Soundtrack':
            return redirect(url_for('mm.jazz'))
        elif met_plz == 'Ambient/Dub/Fourth World':
            return redirect(url_for('mm.amb'))
        elif met_plz == 'Metal/Noise/Experimental':
            return redirect(url_for('mm.metal'))

    metal_mood_form = ChangeMood()
    if request.method == 'POST' and metal_mood_form.validate_on_submit():
        metty_m = User.query.get(current_user.id)
        metty_m_plz = request.form['mood']
        metty_m.mood = metty_m_plz
        db.session.commit()
        flash('Your mood has been updated!', 'euser-created')

    metal1 = ['the_Quietus','quietus-mix-75-pete-swansons-mutations-modernisations']
    metal4 = ['lordnoize','nu-metal-classics']
    metal3 = ['NTSRadio', 'witching-hour-stoner-metal-special']
    metal2 = ['NTSRadio', 'axcess-amnesia-black-metal-xmas-w-dj-necrotik-julhag-dj-satanaas-helper-25th-december-2020']
    metal5 = ['NTSRadio', 'blackest-ever-black-2nd-january-2018']
    metal6 = ['NTSRadio', 'midnite-madness-doom-metal-special-6th-may-2015']
    metal7 = ['GhostWaveRadio', 'welcome-to-the-asylum-february-2021-black-metal']  
    
    greeting = "Metal/Noise/Experimental"
    greeting2 = current_user.mood
    artist = []
    song = []

    if current_user.mood == 'Morning Coffee':
        artist = metal1[0]
        song = metal1[1]
    elif current_user.mood == 'Afternoon Walk':
        artist = metal2[0]
        song = metal2[1]
    elif current_user.mood == 'Dinner with Friends':
        artist = metal3[0]
        song = metal3[1]
    elif current_user.mood == 'Late Night':
        artist = metal4[0]
        song = metal4[1]
    elif current_user.mood == 'Contemplative':
        artist = metal5[0]
        song = metal5[1]
    elif current_user.mood == 'Reading the News':
        artist = metal6[0]
        song = metal6[1]
    elif current_user.mood == 'Driving in a Hurry':
        artist = metal7[0]
        song = metal7[1]
    elif current_user.mood == 'Facial Recognition Mode':
        return redirect(url_for('mm.snap'))


    req = requests.get(f"https://www.mixcloud.com/oembed/?url=https%3A%2F%2Fwww.mixcloud.com%2F{artist}%2F{song}%2F&format=json")
    var1 = json.loads(req.content)
    new = var1['html']
    
    
    
    return render_template("metal.html", new = new, greeting = greeting, greeting2 = greeting2, metal_genre_form = metal_genre_form, metal_mood_form = metal_mood_form)
    


@mm.route('/signin', methods = ['GET', 'POST'])
def signin():

    form2 = UserSigninForm()
    default = ""

    try:
        if request.method == 'POST' and form2.validate_on_submit():
            email = form2.email.data
            password = form2.password.data

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('Welcome back!', 'auth-success')

                if current_user.genre == 'House/Techno/Jungle/Drum n Bass':
                    return redirect(url_for('mm.club'))
                elif current_user.genre == 'Ambient/Dub/Fourth World':
                    return redirect(url_for('mm.amb'))
                elif current_user.genre == 'Jazz/World/Soundtrack':
                    return redirect(url_for('mm.jazz'))
                elif current_user.genre == 'Rock/Pop/Folk':
                    return redirect(url_for('mm.pop'))
                elif current_user.genre == 'Metal/Noise/Experimental':
                    return redirect(url_for('mm.metal'))
                
                
                return redirect(url_for(f'mm.{default}'))
            else:
                flash('Invalid credentials!', 'auth-failed')
                return redirect(url_for('mm.signin'))
    except:
        raise Exception('Invalid')

    return render_template('signin.html', form2 = form2)



@mm.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('mm.home'))