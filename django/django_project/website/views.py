from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext
from django.contrib import messages

from random import randint

import psycopg2

# Create your views here.

def getSymptomOccurance(drug):
	try:
		conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='As4g98HO8J'")
	except:
		print "I am unable to connect to the database. Obviously, this shouldn't print, but why not?"

	cur = conn.cursor()
	cur.execute("""
		SELECT symptom, count(symptom) from website_drugtweet WHERE drug = '{}' GROUP BY symptom
	""".format(drug))

	rows = cur.fetchall()
	dict = {}
	for row in rows:
		dict[row[0]] = {str(row[0]) : int(row[1])}
	return dict

def getPieChart(drug):
	foo = getSymptomOccurance(drug)
	arg1 = "["
	for k, v in foo.iteritems():
		arg1 = arg1 + "['" + k + "'," + str(v[k]) + "],"
	arg1 = arg1 + "]"	
	return arg1

def getBarChart(drug):
	foo = getSymptomOccurance(drug)
	arg2 = "["
	for k, v in foo.iteritems():
		arg2 = arg2 + "['" + k + "', "  + str(v[k]) + " , 'silver'],"
	return arg2

def getWordCloud(drug):
	foo = getSymptomOccurance(drug)
	arg3 = "'"
	for k, v in foo.iteritems():
		arg3 = arg3  + str(v[k]) + "" + k + "\\n" 
	arg3 = arg3[:-1]
	arg3 = arg3 + "n'"
	return arg3

def index(request):
	lomo_string = "Enter your drug:"
	return render(request, 'website/index.html', {'lomo' : lomo_string})

def symptom_string(string):
	advair_string = ' chronic obstructive  pulmonary disease  pulmonary disease  disease  fluticasone  ventolin    ventolin  mild asthma   asthma      giant    ventolin  ventolin  t t t t t t t t t t t t t t t t t t t ventolin  t ventolin  ventolin  singulair  prevacid  gerd        ventolin  ventolin  ventolin   cataracts   ventolin       mild asthma  asthma  kerr    asthma  ventolin   fluticasone salmeterol  fluticasone salmeterol  inflammation  asthma  back asthma  prednisone   singulair  albuterol   affects      ventolin    ventolin      ventolin  hfa  ventolin  adidas    ventolin  asthmatic   asthma  mild asthma   asthma      adidas      ventolin      mild asthma   asthma             ventolin  android android  albuterol mild asthma   asthma  inflammation asthma back android  inflammation  asthma  back  ventolin  ventolin  ventolin       t  ventolin     mild asthma asthma       ventolin  android'
	crestor_string = '  diabetes  lipitor r    lipitor vitamin d      joint pain   joint pain    today  joint pain   joint pain retire   vision     dr   r   r   r      thought   cholesterol r   r   r   r    simvastatin    thought   ar ar  im  cholesterol cholesterol cholesterol    cholesterol lipitor   cholesterol  confusion  rosuvastatin    name  imdur   pneumonitis    rhabdomyolysis    ad    diabetes      chronic  controlled  disease disease   rosuvastatin calcium rosuvastatin calcium  f rosuvastatin   penis paranoia     heart diltiazem accupril norvasc  zetia actos plavix amaryl   dr  liver pain ski     cirrhosis rosuvastatin  diabetes t  cholesterol zetia  liver   side effect side effect cholesterol side effect side effect side effect side effect side effect side effect side effect side effect side effect side effect side effect side effect side effect side effect cholesterol cholesterol dysentery     m '
	cymbalta_string = '         worse            flexeril   fibromyalgia lyrica  aggressiveness  sildenafil  night sweats sweats   paxil female   dream nightmare   dream nightmare duloxetine  synaptic transmission          ba       t    viagra     pain  del  injury  pain management effexor worse latuda lamictal risperdal zyprexa seroquel prozac klonopin  diabetes diabetes memory duloxetine duloxetine duloxetine duloxetine  happy tremors suicidal thoughts suicidal thoughts prozac    depression depression   fluoxetine  depression depression  lamotrigine pain thought dysthymic disorder disorder depression depression pms  es   program  t sns sns depression depression pms happy t t depression depression fast   withdrawal symptoms symptoms prozac  effexor xr          depression depression depersonalization disorder depersonalization disorder  duloxetine oral  withdrawal symptoms symptoms name duloxetine  ibuprofen  name duloxetine  ibuprofen depression depression  xanax depersonalization disorder depersonalization disorder           depression depression  xanax  pain tramadol celebrex  depersonalization disorder depersonalization disorder   prozac  effexor xr effexor  withdrawal symptoms symptoms depression depression   pain      prozac    depersonalization disorder depersonalization disorder  depersonalization disorder depersonalization disorder  r  t        direction depression depression  xanax           adhd  lexapro           depression depression  xanax     brain  lexapro    t nursing  t elderly affects depression depression affects worse  duloxetine fluoxetine depression depression  depression depression scalp stomach depression depression'
	diovan_string = ' isradipine calcium     m love estar     rid  rid  rid rid        weight gain   m  para   ser dead dia dia dia  hct      m   m   hct  reading   dr  hct   para mas  mas po  hct   para   sexual function    m rls miralax requip  nd cyclobenzaprine  hct    os mas tem    para   hct   hct    hct    hct   hct    hct   hct    hct   os t    atenolol altace dyazide   m   visa    hct    hct   hct   hct    sexual function  mind  sexual function  sexual function cr  hct   para    t para para dos t para mas  sexual function    sexual function  m  m side effect os imagination  hct enlarged uterus uterus tem mas  hct  hypertension    hct   sexual function  hct   para            es para mi      hct   hct   hct   hct  hct  hct  hct     hct              hct   hct  m1  hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct   hct  sexual function  sexual function  side effect f para os mas para mas para t         m dia  m block  m  m  m  vc  m block   m  m  m os  m  m tem   m  m  m  m  m  m  m  m  m  m  m para  m dia  m  m  m nas  m   m vc  m  m  ser mas no  m  m  m cad cough  m digital dos dos  m  m  m nas para   m  vc mas mas ser   m mas   m  po mas   m    m     t mas tem os  tem ra ser tem  t os ser dia   t placebo         m   m   m dos no tem   m yes   m  mas para   m   m   m   m mao   m   m mas tem  para ll    m   m  mas t     po  sil   tem tem mds os  m t'
	lantus_solostar_string = '  apidra novolog fix           apidra dos   cancer apidra   apidra humalog  apidra   m  m apidra humalog  apidra humalog  apidra   apidra  apidra    celexa disease disorder   apidra  novolog diabetes insulin  insulin diabetes insulin burning sensation sensation  diabetes insulin novolog  diabetes insulin  insulin glargine insulin diabetes insulin  mas r  no     insulin glargine insulin diabetes insulin  novolog  diabetes insulin para   red  blood levemir work   red relief    burning sensation sensation  diabetes insulin   para   cancer bac    diabetes      subconscious apidra insulin   apidra novolog fix   pcp      all    diabetes   insulin insulin  apidra  para diabetes  humalog today            diabetes insulin  hearts    interested reading    management    cancer      novolog     para bo dos  '
	lyrica_string = '       rp         thinking  nothing         face blade  feeling worse     paw paw eyes        eyes       angry     red            sits hooves   walks  confused     yes  hooves head  walks    back head runs walks   walk          climbs climbs     face  eyes nothing      nothing     back    head branch   eyes     cheek red back    face eyes red    mind  nerve pain epilepsy fibromyalgia pushes   claws neck      sad sad nerve pain epilepsy fibromyalgia t running  jumps jumping   walks              paw paw  sad sad       nerve pain epilepsy fibromyalgia pinkie alive     females  cake     r today   t  geodon zyvox  neurontin detrol lipitor      pregabalin depakote er depakote er fibromyalgia  cymbalta    sex love happy  celebrex effexor lipitor  viagra xanax zoloft    fibromyalgia   hair    rb adidas               pain             t  tattoo         mind fibromyalgia            sns                   cr econazole cr  lioresal pariet        geodon zyvox  neurontin detrol lipitor  diabetes insulin name cramps  emotions today   crestor  pariet cr tegretol   econazole pariet les  les cr econazole cr  lioresal cr pariet cr  pariet econazole cr  np                    vicodin      heart        today        cr econazole cr  lioresal pariet        geodon zyvox  neurontin detrol lipitor  diabetes insulin name cramps  emotions today  '
	nexium_string = '       para mi    prilosec omeprazole   prevacid     maalox tagamet prilosec   maalox tagamet prilosec    nothing    ph   reflux         para mi       bd       para mi    para           bd         para mi      para mi  bd               para mi        para mi        para mi                        para mi      para mi      para mi         para mi       lens nas ar ar t ba    yaz ger ba hep     mi       para   para   para   para   para   para    para   para   para   para   para   para   para   para   para   para                 symptoms gerd acid reflux reflux cancer   heartburn   r          prilosec           m  olan  m   ad  olan    ba hep nas t  ad      nd metronidazole     hep       para   hair loss hair   para   para ser           hand                     nothing     nothing     prilosec     tums        oral pain score pain   ba  m   m  m     ad     m para      ger er    work             appendix appendix   m appendix appendix normal appendix appendix  mi  appendix appendix ad nas ad ba appendix appendix              head            hand   ba ba   t      m        adl ba hep   bo    ba   ger   aciphex    m         ibs     heartburn                       para             name     direction ibs       heartburn    digestive   m  dr       m ibs         name   m  m     pepcid  yaz      name       name               heartburn gastroesophageal reflux disease gastroesophageal reflux reflux disease gerd       name        ibs             stomach pain stomach pain heartburn gastroesophageal reflux disease gastroesophageal reflux reflux disease gerd     nas           content     stomach pain stomach pain    m          dia         thrombocytopenia    name   ar ar    name     ad   name         acid reflux reflux     judgment   judgment            yes                          prilosec   antagonist tumor                      heart burn       penis   stomach             bone fracture bone fracture   bone fracture bone fracture                ulcers issue   issue    '
	synthroid_string = '     t4       thyroid            weight loss  weight loss  weight loss  weight loss  weight loss            weight loss  weight loss  weight loss  weight loss  weight loss        eltroxin     hair loss hair     memory thyroid thyroid   depression depression   thyroid problem    thyroid symptoms             zetia aspirin       cytomel    iodine  name       np  cytomel  labs  cytomel metformin  hypothyroid vitamin d      labs      armour thyroid thyroid    disease   yes   pain       ms     para     dreams  armour thyroid thyroid   thyroid t4  thyroid  t4 t4 hypothyroidism symptoms  energy   hypothyroid  kerr  thyroid thyroid  thyroid      rest moods      m   thyroid condition hypothyroid symptoms   normal metabolism chest pains chest  weight loss weight loss weight loss       hair loss hair natural thyroid thyroid thyroid         t4 westhroid  weight loss weight loss weight loss ear  thyroid cancer thyroid cancer ear  thyroid cancer thyroid cancer does weight loss weight loss weight loss weight loss weight loss   thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer all symptoms  thyroid cancer thyroid cancer  weight loss weight loss weight loss    thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer  thyroid cancer thyroid cancer birth  thyroid cancer thyroid cancer thyroiditis hypothyroidism thyroiditis hypothyroidism thyroid hypothyroidism read back fingernails      thyroid cancer thyroid cancer  hypothyroid  weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss thyroid  hypothyroidism  weight loss happy weight loss happy weight loss happy weight loss happy weight loss happy weight loss happy weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss hypothyroidism hypothyroidism  energy weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss weight loss  hypothyroid  weight loss weight loss happy weight loss happy weight loss weight loss weight loss weight loss weight loss Weight Loss'
	ventolin_string = '   hfa symbicort heart disease heart disease nose bleeds nose exercise para para pneumonia  hfa asthma attack asthma attack  hfa pregnancy t cough pregnant pneumonia para lung damage   administration  hfa  hfa  pregnancy      atrovent           hfa    symbicort    heart disease heart disease atrovent   nose bleeds nose   exercise   loratadine    aerosol     para   combivent   para  pneumonia      hfa    atrovent       asthma attack asthma attack   hfa  pregnancy alvesco        t       cough    pregnant pneumonia  para   lung damage     administration        hfa    propranolol     theophylline  atrovent   hfa        pregnancy   para        asthma    prednisone   hfa     hair loss hair         nebules   nebules    para      asthma attack asthma attack   dry cough dry cough     nebules         albuterol  nebules   hfa   oral    hair loss hair  hfa     t   hfa  cough     evohaler     pregnancy    symbicort   flovent    pregnant  normal  atrovent            snoring   seizures    cough  dr dip dr dip    ep      hfa      para        asthma    prednisone   hfa     hair loss hair         nebules   nebules    para      asthma attack asthma attack   dry cough dry cough     nebules         albuterol  nebules   hfa   oral    hair loss hair  hfa     t   hfa  cough     evohaler     pregnancy    symbicort   flovent    pregnant  normal  atrovent            snoring   seizures    cough  dr dip dr dip    ep      hfa     t normal inhalation  ibu interaction anxiety anxiety ibu cardiovascular para pregnant  es proair hfa  hfa proair hfa  hfa cfc  oral sport  hfa cough pregnancy expiration fast es  hfa pregnancy overdose  nebules  hfa expiration  tb nursing delirium  hfa  pregnancy metallic taste taste  hfa  nebules t normal inhalation  ibu interaction anxiety anxiety ibu cardiovascular para pregnant  es proair hfa  hfa proair hfa  hfa cfc  oral sport  hfa cough pregnancy expiration fast es  hfa pregnancy overdose  nebules  hfa expiration  tb nursing delirium  hfa  pregnancy metallic taste taste  hfa  nebules insomnia  para pregnancy symbicort metabolism blood pressure blood pressure  hfa expiration photosensitivity work media interaction para  male ibu bronchitis del sport para  hfa expiration para  m  hfa  hfa  evohaler  hfa hands  hfa delirium  hfa allergies interaction oral liquid avant mi  insomnia  para pregnancy symbicort metabolism blood pressure blood pressure  hfa expiration photosensitivity work media interaction para  male ibu bronchitis del sport para  hfa expiration para  m  hfa  hfa  evohaler  hfa hands  hfa delirium  hfa allergies interaction oral liquid avant mi        eia       dry cough dry cough benadryl   inderal     asthma     hfa  expiration         para   ibu lips  hfa  eyes   flovent       para  hfa   anaphylaxis metoprolol  interaction        para   acid reflux reflux      hfa       asthma  agus   overdose  chronic cough cough    croup       aerosol   budesonide  flixotide   aerosol       hfa  cough     sleepy    bronchitis   albuterol     aerosol    nas    exercise   hfa        eia       dry cough dry cough benadryl   inderal     asthma     hfa  expiration         para   ibu lips  hfa  eyes   flovent       para  hfa   anaphylaxis metoprolol  interaction        para   acid reflux reflux      hfa       asthma  agus   overdose  chronic cough cough    croup       aerosol   budesonide  flixotide   aerosol       hfa  cough     sleepy    bronchitis   albuterol     aerosol    nas    exercise   hfa '
	vyvanse_string = '        crack crack cocaine  concerta ritalin      m      im            head    cup  anxiety anxiety worse      weight loss  adderall   adderall  adderall     love           binge-eating  disease    dis dis          wellbutrin  amen   wellbutrin  nalex  wide awake awake        disorder  strattera    ambien    dead    energy                  adderall            viagra thinking   drive   adderall  amphetamine    motrin  adderall  cleaning    ain t               tomorrow          adderall        work     ain t   sleep anxiety anxiety planning fall n1 work   anxiety anxiety   anxiety anxiety anxiety anxiety   sleep  anxiety anxiety  adhd death side effect            m     m    drunk  drunk sleep im  block  binge eating eating disease        work    feeling  insomnia work tomorrow    adhd  binge-eating disease sucks        anxiety anxiety head  eat    m ll  love          m sleepy      binge-eating disorder binge-eating disorder  weak            fingernails work             sleep    back  monster   binge-eating disease t    ain t  ll  mood klonopin pack klonopin         writing  working outlook             mood   dig swimming nothing brain   dr adhd  personality  motivation sitting accident head heart             anxiety anxiety     ain t  ll  attention  ain t  ll      ain t  ll    red can red can work   sleep          m wide awake awake brain  thoughts   cleaning attitude cleaning cleaning     does face   im mental handicap handicap    awake       m   m       hungry    im   tomorrow    sit                     im     ll  mood  hydrocodone nothing  t  hydrocodone love paranoia urination      normal    energy  stomach stomach hunger hand work   nothing work      im lungs media      adhd       thinking    work   yes   thoughts binge-eating disease t   binge-eating eating disease back      binge-eating disease t'

	if string == 'advair':
		return advair_string
	if string == 'crestor':
		return crestor_string
	if string == 'cymbalta':
		return cymbalta_string
	if string == 'diovan':
		return diovan_string
	if string == 'lantus solostar':
		return lantus_solostar_string
	if string == 'lyrica':
		return lyrica_string
	if string == 'nexium':
		return nexium_string
	if string == 'synthroid':
		return synthroid_string
	if string == 'ventolin':
		return ventolin_string
	if string == 'vyvanse':
		return vyvanse_string
	return string

def wordcloud(request):
	drug = request.GET['drug_name'].lower()
	return render(request, 'website/wordcloudv2.html', {'aihoa' : getWordCloud(drug) })

def result(request):
	listOfValidDrugs = ['advair', 'crestor', 'cymbalta', 'diovan', 'lantus solostar', 'lyrica', 'nexium', 'synthroid', 'ventolin', 'vyvanse']
	if 'drug_name' in request.GET and request.GET['drug_name']:
		drugs = request.GET['drug_name']
		if drugs.lower() in listOfValidDrugs:
			chart = get_chart(drugs)         	
			return render(request, 'website/result.html', {'chart' : chart, 'drugs' : drugs})
		else:
			return render(request, 'website/index.html', {'error' : 'Unfortunately, this drug does not exist in our databases as of this moment.' })
	else:
		return render(request, 'website/index.html', {'error' : 'Please enter a valid drug.' })

def bar_result(request):
        listOfValidDrugs = ['advair', 'crestor', 'cymbalta', 'diovan', 'lantus solostar', 'lyrica', 'nexium', 'synthroid', 'ventolin', 'vyvanse']
        if 'drug_name' in request.GET and request.GET['drug_name']:
                drugs = request.GET['drug_name']
                if drugs.lower() in listOfValidDrugs:
                        chart = get_silver_chart(drugs)
                        return render(request, 'website/bar_result.html', {'chart' : chart, 'drugs' : drugs})
                else:
                        return render(request, 'website/index.html', {'error' : 'Unfortunately, this drug does not exist in our databases as of this moment.' })
        else:
                return render(request, 'website/index.html', {'error' : 'Please enter a valid drug.' })

def get_chart(request):
	if request.lower() == 'advair':
		return getPieChart(request.lower())
	if request.lower() == 'crestor':
		return getPieChart(request.lower())
	if request.lower() == 'cymbalta':
		return getPieChart(request.lower())
	if request.lower() == 'diovan':
		return getPieChart(request.lower())
	if request.lower() == 'lantus solostar':
		return getPieChart(request.lower())
	if request.lower() == 'lyrica':
		return getPieChart(request.lower())
	if request.lower() == 'nexium':
		return getPieChart(request.lower())	
	if request.lower() == 'synthroid':
		return getPieChart(request.lower())
	if request.lower() == 'ventolin':
		return getPieChart(request.lower())
	if request.lower() == 'vyvanse':
		return getPieChart(request.lower())
	else:
		return [['Cancer', randint(0,9)], ['Cold',  randint(0,9)], ['Fever', randint(0,9)], ['Nausea', randint(0, 9)]]
                
def get_silver_chart(request):
	if request.lower() == 'advair':
		return getBarChart(request.lower())
	if request.lower() == 'crestor':
		return getBarChart(request.lower())
	if request.lower() == 'cymbalta':
		return getBarChart(request.lower())
	if request.lower() == 'diovan':
		return getBarChart(request.lower())
	if request.lower() == 'lantus solostar':
		return getBarChart(request.lower())
	if request.lower() == 'lyrica':
		return getBarChart(request.lower())
	if request.lower() == 'nexium':
		return getBarChart(request.lower())
	if request.lower() == 'synthroid':
		return getBarChart(request.lower())
	if request.lower() == 'ventolin':
		return getBarChart(request.lower())
	if request.lower() == 'vyvanse':
		return getBarChart(request.lower())
	else:
		return [['Cancer', randint(0,9), "silver"], ['Cold',  randint(0,9), "silver"], ['Fever', randint(0,9), "silver"], ['Nausea', randint(0, 9)]]
