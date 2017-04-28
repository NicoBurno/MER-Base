#######################################
#
#	Character generator data
#

 init python:

    genuses_frequency = {
    'human': 10, 
    'undead': 5,
    'doghead': 3,  
    'slime': 2, 
    }


    ages_frequency = {
    'junior': 1,
    'adolescent': 2,
    'mature': 3,   
    'elder': 1,      
    }

    sexes_frequency = {
    'male': 4,
    'female': 5,
    'shemale': 1,   
    'transmale': 1,        		    	    	
    'transfemale': 1,    
    }

    constitutions_frequency = {
	    'default': {
	    	'normal': 5,
	    	'brawny': 3,
	    	'lean': 3,    
	    	'large': 3,    	
	    	'small': 3,
	    	'athletic': 2,
	    	'clumsy': 2,
	    	'crooked': 1, 	    	    	
	    }, 

	    'junior': {
	    	'normal': 3,
	    	'brawny': 0,
	    	'lean': 2,    
	    	'large': 0,    	
	    	'small': 6,
	    	'athletic': 0,
	    	'clumsy': 2,
	    	'crooked': 1, 	    	    	
	    }, 
	    
	    'adolescent': {
	    	'normal': 4,
	    	'brawny': 2,
	    	'lean': 4,    
	    	'large': 2,    	
	    	'small': 4,
	    	'athletic': 2,
	    	'clumsy': 2,
	    	'crooked': 1, 	    	    	
	    }, 

	    'mature': {
	    	'normal': 5,
	    	'brawny': 4,
	    	'lean': 2,    
	    	'large': 4,    	
	    	'small': 2,
	    	'athletic': 3,
	    	'clumsy': 2,
	    	'crooked': 2, 	    	    	
	    }, 

	    'elder': {
	    	'normal': 4,
	    	'brawny': 3,
	    	'lean': 3,    
	    	'large': 2,    	
	    	'small': 4,
	    	'athletic': 1,
	    	'clumsy': 3,
	    	'crooked': 4, 	    	    	
	    }, 
                
    }

    quirks_frequency = {
    'stubborn': 1,
    'sly': 1,
    'careless': 1,  
    'scrupulous': 1,        
    'optimistic': 1,
    'nagging': 1,
    'smart': 1,
    'dumb': 1,
    
    }

    appearance_frequency = {
    	'default': {
    		'unremarkable': 6, 
    		'gentle': 3, 
    		'bold': 3, 
    		'flawless': 2,
    		'coarse': 2, 
    		'naive': 2, 
    		'honest': 2, 
    		'wild': 2, 
    		'foxy': 2, 
    		'sleazy': 2, 
    		'unusual': 1, 
    	},

    	'masculine': {
    		'unremarkable': 6, 
    		'gentle': 2, 
    		'bold': 4, 
    		'flawless': 1,
    		'coarse': 3, 
    		'naive': 2, 
    		'honest': 2, 
    		'wild': 3, 
    		'foxy': 1, 
    		'sleazy': 1, 
    		'unusual': 1, 
    	},

    	'feminine': {
    		'unremarkable': 6, 
    		'gentle': 4, 
    		'bold': 2, 
    		'flawless': 3,
    		'coarse': 2, 
    		'naive': 2, 
    		'honest': 2, 
    		'wild': 1, 
    		'foxy': 3, 
    		'sleazy': 3, 
    		'unusual': 1, 
    	},
    
    }

    sexual_orientation = {
    	'default': {
    		'asexual': 1, 
    	},

    	'masculine': {
    		'asexual': 1, 
    		'omisexual': 2, 
    		'bisexual': 3, 
    		'bicurious_male': 5, 
    		'straight_male': 10,
    		'bicurious_female': 0, 
    		'straight_female': 0, 
    		'gay': 2, 
    		'lesbian': 0, 
    	},

    	'feminine': {
    		'asexual': 1, 
    		'omisexual': 3, 
    		'bisexual': 5, 
    		'bicurious_male': 0, 
    		'straight_male': 0,
    		'bicurious_female': 10, 
    		'straight_female': 5, 
    		'gay': 0, 
    		'lesbian': 3, 
    	},

    }

    sexual_type = {
    	'default': {
    		'frigid': 1, 
    	},

    	'male': {
    		'dissolute': 5, 
    		'worn': 3, 
    		'frigid': 6, 
    		'modest': 10, 
    		'vanilla': 30,
    		'macho': 20, 
    		'caring': 10, 
    		'gentle': 5, 
    		'suitor': 5, 
    		'narcissistic': 3, 
    		'passionate': 20, 
    		'lewd': 20,
    		'vtop': 25, 
    		'vbottom': 5, 
    		'active': 30, 
    		'passive': 10, 
    		'sadist': 10, 
    		'masochist': 5, 
    		'sadomazo': 5,
    		'strict_sadist': 5, 
    		'strict_masochist': 2, 
    		'strict_sadomazo': 3, 
    		'dominant': 10, 
    		'bizzare_dominant': 5, 
    		'bizzare_submissive': 3, 
    		'switch': 6,
    		'kniky': 10, 
    		'wild_kinky': 2, 
    		'tender_switch': 3, 
    		'wild': 4,   
    		'freak': 2, 
    		'deviant': 2, 
    		'loony': 1, 
    		'weirdo': 1,      		  		    		    		
    	},

    	'female': {
    		'dissolute': 3, 
    		'worn': 6, 
    		'frigid': 10, 
    		'modest': 20, 
    		'vanilla': 30,
    		'macho': 0, 
    		'caring': 25, 
    		'gentle': 15, 
    		'suitor': 10, 
    		'narcissistic': 2, 
    		'passionate': 20, 
    		'lewd': 15,
    		'vtop': 5, 
    		'vbottom': 25, 
    		'active': 10, 
    		'passive': 30, 
    		'sadist': 5, 
    		'masochist': 10, 
    		'sadomazo': 7,
    		'strict_sadist': 2, 
    		'strict_masochist': 5, 
    		'strict_sadomazo': 3, 
    		'dominant': 5, 
    		'bizzare_dominant': 2, 
    		'bizzare_submissive': 5, 
    		'switch': 15,
    		'kniky': 5, 
    		'wild_kinky': 2, 
    		'tender_switch': 3, 
    		'wild': 2,   
    		'freak': 2, 
    		'deviant': 2, 
    		'loony': 1, 
    		'weirdo': 1,      		  		    		    		
    	},

    	'shemale': {
    		'dissolute': 5, 
    		'worn': 3, 
    		'frigid': 6, 
    		'modest': 10, 
    		'vanilla': 30,
    		'macho': 20, 
    		'caring': 10, 
    		'gentle': 5, 
    		'suitor': 5, 
    		'narcissistic': 3, 
    		'passionate': 20, 
    		'lewd': 20,
    		'vtop': 25, 
    		'vbottom': 5, 
    		'active': 30, 
    		'passive': 10, 
    		'sadist': 10, 
    		'masochist': 5, 
    		'sadomazo': 5,
    		'strict_sadist': 5, 
    		'strict_masochist': 2, 
    		'strict_sadomazo': 3, 
    		'dominant': 10, 
    		'bizzare_dominant': 5, 
    		'bizzare_submissive': 3, 
    		'switch': 6,
    		'kniky': 10, 
    		'wild_kinky': 2, 
    		'tender_switch': 3, 
    		'wild': 4,   
    		'freak': 2, 
    		'deviant': 2, 
    		'loony': 1, 
    		'weirdo': 1,      		  		    		    		
    	},

    	'transmale': {
    		'dissolute': 3, 
    		'worn': 6, 
    		'frigid': 10, 
    		'modest': 20, 
    		'vanilla': 30,
    		'macho': 0, 
    		'caring': 25, 
    		'gentle': 15, 
    		'suitor': 10, 
    		'narcissistic': 2, 
    		'passionate': 20, 
    		'lewd': 15,
    		'vtop': 5, 
    		'vbottom': 25, 
    		'active': 10, 
    		'passive': 30, 
    		'sadist': 5, 
    		'masochist': 10, 
    		'sadomazo': 7,
    		'strict_sadist': 2, 
    		'strict_masochist': 5, 
    		'strict_sadomazo': 3, 
    		'dominant': 5, 
    		'bizzare_dominant': 2, 
    		'bizzare_submissive': 5, 
    		'switch': 15,
    		'kniky': 5, 
    		'wild_kinky': 2, 
    		'tender_switch': 3, 
    		'wild': 2,   
    		'freak': 2, 
    		'deviant': 2, 
    		'loony': 1, 
    		'weirdo': 1,      		  		    		    		
    	},

    	'transfemale': {
    		'dissolute': 5, 
    		'worn': 3, 
    		'frigid': 6, 
    		'modest': 10, 
    		'vanilla': 30,
    		'macho': 20, 
    		'caring': 10, 
    		'gentle': 5, 
    		'suitor': 5, 
    		'narcissistic': 3, 
    		'passionate': 20, 
    		'lewd': 20,
    		'vtop': 25, 
    		'vbottom': 5, 
    		'active': 30, 
    		'passive': 10, 
    		'sadist': 10, 
    		'masochist': 5, 
    		'sadomazo': 5,
    		'strict_sadist': 5, 
    		'strict_masochist': 2, 
    		'strict_sadomazo': 3, 
    		'dominant': 10, 
    		'bizzare_dominant': 5, 
    		'bizzare_submissive': 3, 
    		'switch': 6,
    		'kniky': 10, 
    		'wild_kinky': 2, 
    		'tender_switch': 3, 
    		'wild': 4,   
    		'freak': 2, 
    		'deviant': 2, 
    		'loony': 1, 
    		'weirdo': 1,      		  		    		    		
    	},

    }    

##############################################################################
# Names
#
# Random names lists for generic characters

    firstname = {
        'default': {
            'male': [__('Jack'), __('Michael'),__('Andrew'),__('Daniel'),__('Billy'),
            __('Willie'),__('Jose'),__('John'),__('Nilkolas'),__('Alex'),__('Sam'),
            ],
            'female': [__('Hanna'),__('Mary'),__('Enny'),__('Emma'),__('Samantha'),
            __('Anna'),__('Sara'),__('Sophia'),__('Viktoria'),__('Julia'),
            ]
        },
    
        'slavic': {
            'male': [__('Avdey'), __('Agap'),__('Akim'),__('Andron'),__('Onisim'),
            __('Antyp'),__('Bajen'),__('Bogdan'),__('Boleslav'),__('Boyan'),
            __('Broneslav'),__('Budimir'),__('Velimir'),__('Vikenty'),__('Vladislav'),            
            __('Vlas'),__('Vsevolod'),__('Vsemil'),__('Vseslav'),__('Vysheslav'),        
            __('Gavrila'),__('Gerasim'),__('Gleb'),__('Gordey'),__('Gostomysl'),        
            __('Gremislav'),__('Dementy'),__('Demyan'),__('Dobromysl'),__('Dobroslav'),        
            __('Dorofey'),__('Evgraf'),__('Evdokim'),__('Evsey'),__('Evlampy'),                    
            __('Evstafy'),__('Elisey'),__('Eremey'),__('Evril'),__('Ermolay'),            
            __('Erofey'),__('Efim'),__('Efrem'),__('Ignat'),__('Izot'),        
            __('Izyaslav'),__('Illaryon'),__('Ipaty'),__('Lavr'),__('Ladymir'),        
            __('Lukyan'),__('Luchezar'),__('Lukyan'),__('Lybim'),__('Lubomir'),        
            __('Lubomysl'),__('Makar'),__('Martyn'),__('Matvey'),__('Mifody'),     
            __('Mechislav'),__('Miron'),__('Miroslav'),__('Mstislav'),__('Nazar'),            
            __('Natan'),__('Nestor'),__('Nikanor'),__('Nikola'),__(''),        
            __('Pankrat'),__('Panteley'),__('Panfil'),__('Pakhom'),__('Prokhor'),        
            __('Radislav'),__('Radovan'),__('Ratibor'),__('Ratmir'),__('Rostislav'),        
            __('Taras'),__('Tverdislav'),__('Terenty'),__('Timofey'),__('Tykhon'),     
            __('Tryphon'),__('Trofim'),__('Ylyan'),__('Fadey'),__('Fedot'),            
            __('Feofan'),__('Philimon'),__('Foma'),__('Frol'),__('Khariton'),   
            __('Alexander'), __('Alexy'),__('Anatoly'),__('Andrey'),__('Anton'),
            __('Arkady'),__('Anton'),__('Artem'),__('Boris'),__('Bogdan'),
            __('Vadim'),__('Valentin'),__('Valery'),__('Vasily'),__('Viktor'),            
            __('Vyacheslav'),__('Genady'),__('Georgy'),__('Grigory'),__('Evgeny'),        
            __('Ivan'),__('Igor'),__('Ilya'),__('Kirill'),__('Lev'),        
            __('Leonid'),__('Maksim'),__('Mark'),__('Mikhail'),__('Nikita'),        
            __('Pavel'),__('Petr'),__('Potap'),__('Roman'),__('Ruslan'),                    
            __('Timur'),__('Fedor'),__('Philipp'),__('Uriy'),__('Uliy'),       
            ],
            'female': [__('Avdotya'),__('Aksinya'),__('Bajena'),__('Bogdana'),__('Boleslava'),
            __('Vasilina'),__('Vasilisa'),__('Vlada'),__('Vlasta'),__('Vladilena'),
            __('Volya'),__('Vseslava'),__('Goluba'),__('Gorislava'),__('Dobrava'),
            __('Efrosinya'),__('Jdana'),__('Zarina'),__('Zoryana'),__('Zvenislava'),            
            __('Zlata'),__('Iskra'),__('Klara'),__('Klavdia'),__('Lada'),        
            __('Lesya'),__('Lybomira'),__('Marfa'),__('Matrena'),__('Melania'),        
            __('Milana'),__('Militsa'),__('Miloslava'),__('Miroslava'),__('Mlada'),        
            __('Mstislava'),__('Praskovia'),__('Rada'),__('Radmila'),__('Svetlana'),                    
            __('Svetozara'),__('Svoboda'),__('Svyatoslava'),__('Slava'),__('Slavyana'),            
            __('Snezhana'),__('Uliana'),__('Ustinia'),__('Uslada'),__(''),        
            __('Yaroslava'), __('Agnia'),__('Alexandra'),__('Alena'),__('Alina'),__('Alisa'),
            __('Alla'),__('Anastasya'),__('Anna'),__('Valentina'),__('Valeria'),
            __('Varvara'),__('Vera'),__('Viktoria'),__('Darya'),__('Diana'),            
            __('Evgenia'),__('Ekaterina'),__('Elena'),__('Elisaveta'),__('Janna'),        
            __('Zoya'),__('Zina'),__('Inga'),__('Inna'),__('Irina'),        
            __('Katerina'),__('Kira'),__('Kristina'),__('Ksenya'),__('Larisa'),        
            __('Lida'),__('Lina'),__('Ludmila'),__('Lybov'),__('Malvina'),                    
            __('Mrina'),__('Marya'),__('Nadezhda'),__('Nastya'),__('Natalia'),            
            __('Nora'),__('Oksana'),__('Olesya'),__('Olga'),__('Polina'),        
            __('Raisa'),__('Regina'),__('Renata'),__('Rosa'),__('Sveta'),        
            __('Sofia'),__('Tamara'),__('Tatiana'),__('Kristina'),__('Uylia'),        
            __('Yana'),     
            ]
        },

        'western': {
            'male': [__('Adolf'), __('Adrian'),__('Alen'),__('Alfons'),__('Aler'),
            __('Ambraus'),__('Anatole'),__('Andrian'),__('Andre'),__('Arman'),
            __('Arno'),__('Astor'),__('Antanas'),__('Basile'),__('Baptist'),            
            __('Barnaby'),__('Bastian'),__('Besenet'),__('Bernard'),__('Bleiz'),        
            __('Boduen'),__('Boniface'),__('Brees'),__('Valentine'),__('Gay'),        
            __('Gaston'),__('Gaspard'),__('Godard'),__('Gilbert'),__('Guilem'),        
            __('Gustav'),__('Denis'),__('Jeremy'),__('Joseph'),__('Jory'),     
            __('Dominique'),__('Jacque'),__('Jan'),__('Jerom'),__('Jile'),            
            __('Jerard'),__('Joffrua'),__('Julian'),__('Ivon'),__('Kamil'),        
            __('Klementh'),__('Kolombo'),__('Kristoff'),__('Lasare'),__('Lionel'),        
            __('Leonard'),__('Leopold'),__('Lorence'),__('Lotar'),__('Luie'),        
            __('Luke'),__('Lucian'),__('Maximilian'),__('Matice'),__('Morrice'),     
            __('Nikolas'),__('Nihel'),__('Oberon'),__('Olyvier'),__('Paskal'),            
            __('Ogasten'),__('Odrik'),__('Patrice'),__('Parcifale'),__('Raimondo'),        
            __('Raul'),__('Renard'),__('Robert'),__('Rojer'),__('Roderik'),        
            __('Roland'),__('Sverus'),__('Cesare'),__('Stefano'),__('Theo'),        
            __('Tyerri'),__('Fabis'),__('Felix'),__('Fabian'),__('Phillippe'),    
            __('Forest'),__('Frank'),__('Hamon'),__('Honor'),__('Chrles'),            
            __('Edvard'),__('Emerik'),__('Etien'),__('Judes'),__('Jurben'),        
            __('Adelstain'),__('Adler'),__('Albert'),__('Alfonce'),__('Arnold'),        
            __('Bertold'),__('Willie'),__('Wolf'),__('Wolfgang'),__('Ganse'),        
            __('Gunter'),__('Godric'),__('Genrich'),__('Gerorge'),__('Gottfold'),    
            __('Ditrich'),__('Karl'),__('Johan'),__('Kristof'),__('Leopold'),            
            __('Markus'),__('Nikolas'),__('Zigberd'),__('Ulrich'),__('Urgen'),        
            __('Vito'),__('Gonzalo'),__('Gustavo'),__('Havier'),__('Julian'),        
            __('Diego'),__('Dimas'),__('Donato'),__('Domingo'),__('Jose'),        
            __('Karlito'),__('Karlos'),__('Krisobal'),__('Luis'),__('Patricio'),     
            __('Jacob'), __('Mason'),__('Ethan'),__('Noah'),__('William'),
            __('Liam'),__('Jayden'),__('Michael'),__('Alexander'),__('Aiden'),
            __('Daniel'),__('Matthew'),__('Elijah'),__('James'),__('Anthony'),
            __('Benjamin'),__('Joshua'),__('Andrew'),__('David'),__('Joseph'),            
            __('Logan'),__('Jackson'),__('Christopher'),__('Gabriel'),__('Samuel'),        
            __('Ryan'),__('Lucas'),__('John'),__('Nathan'),__('Isaac'),        
            __('Dylan'),__('Caleb'),__('Christian'),__('Landon'),__('Jonathan'),        
            __('Carter'),__('Luke'),__('Owen'),__('Brayden'),__('Gavin'),     
            __('Wyatt'),__('Isaiah'),__('Henry'),__('Eli'),__('Hunter'),            
            __('Jack'),__('Evan'),__('Jordan'),__('Nicholas'),__('Tyler'),        
            __('Aaron'),__('Jeremiah'),__('Julian'),__('Cameron'),__('Levi'),        
            __('Brandon'),__('Angel'),__('Austin'),__('Connor'),__('Adrian'),        
            __('Robert'),__('Charles'),__('Thomas'),__('Sebastian'),__('Colton'),     
            __('Jaxon'),__('Kevin'),__('Zachary'),__('Ayden'),__('Dominic'),            
            __('Blake'),__('Jose'),__('Oliver'),__('Justin'),__('Bentley'),        
            __('Jason'),__('Chase'),__('Ian'),__('Josiah'),__('Parker'),        
            __('Xavier'),__('Adam'),__('Cooper'),__('Nathaniel'),__('Grayson'),        
            __('Jace'),__('Carson'),__('Nolan'),__('Tristan'),__('Luis'),    
            __('Brody'),__('Juan'),__('Hudson'),__('Bryson'),__('Carlos'),            
            __('Easton'),__('Damian'),__('Alex'),__('Kayden'),__('Ryder'), 
            ],

            'female': [__('Abelia'),__('Abel'),__('Avrora'),__('Agnes'),__('Adele'),
            __('Alexandra'),__('Ammaranthe'),__('Anastasia'),__('Angelique'),__('Annete'),
            __('Anette'),__('Aurelie'),__('Barbara'),__('Bernadette'),__('Blanche'),
            __('Brigitte'),__('Valentine'),__('Valerie'),__('Victoria'),__('Virgine'),            
            __('Gabriella'),__('Gvinniver'),__('Godelif'),__('Daniela'),__('Dafna'),        
            __('Denise'),__('Jine'),__('Jinnet'),__('Joel'),__('Josie'),        
            __('Julie'),__('Juliette'),__('Justine'),__('Dominique'),__('Dorotea'),        
            __('Jaquline'),__('Jen'),__('Julien'),__('Zoe'),__('Ivette'),     
            __('Ivonne'),__('Inesse'),__('Iren'),__('Izidore'),__('Kamilla'),            
            __('Karol'),__('Kler'),__('Kolette'),__('Katrine'),__('Kristine'),        
            __('Lidy'),__('Lillian'),__('Lulu'),__('Madlene'),__('Megane'),        
            __('Melisa'),__('Morgane'),__('Merrion'),__('Nadia'),__('Ninnet'),        
            __('Noel'),__('Orabel'),__('Peneloppe'),__('Poline'),__('Polette'),     
            __('Rosalie'),__('Sabina'),__('Simonete'),__('Sophie'),__('Stephanie'),            
            __('Susette'),__('Felicia'),__('Helen'),__('Khloya'),__('Florette'),        
            __('Chantalle'),__('Charlotte'),__('Evette'),__('Evone'),__('Elison'),        
            __('Emily'),__('Enn'),__('Estel'),__('Eloise'),__('Elise'),        
            __('Abigail'),__('Agate'),__('Alba'),__('Angela'),__('Beatrice'),    
            __('Blanka'),__('Veronique'),__('Gracia'),__('Debora'),__('Delphine'),            
            __('Dorotea'),__('Isabelle'),__('Konchitta'),__('Luise'),__('Marcelle'),        
            __('Miquelle'),__('Monique'),__('Mirabella'),__('Ophelia'),__('Ramona'),        
            __('Alina'),__('Alberthine'),__('Belinde'),__('Brunhild'),__('Gretta'),        
            __('Zelda'),__('Isolde'),__('Irma'),__('Karoline'),__('Lisa'),     
            __('Raphaella'),__('Susie'),__('Ulrike'),__('Franciska'),__('Hilde'),
            __('Sophia'),__('Emma'),__('Isabella'),__('Olivia'),__('Ava'),
            __('Emily'),__('Abigail'),__('Mia'),__('Madison'),__('Elizabeth'),
            __('Chloe'),__('Ella'),__('Avery'),__('Addison'),__('Aubrey'),
            __('Lily'),__('Natalie'),__('Sofia'),__('Charlotte'),__('Zoey'),            
            __('Grace'),__('Hannah'),__('Amelia'),__('Harper'),__('Lillian'),        
            __('Samantha'),__('Evelyn'),__('Victoria'),__('Brooklyn'),__('Zoe'),        
            __('Layla'),__('Hailey'),__('Leah'),__('Kaylee'),__('Anna'),        
            __('Aaliyah'),__('Gabriella'),__('Allison'),__('Nevaeh'),__('Alexis'),     
            __('Audrey'),__('Savannah'),__('Sarah'),__('Alyssa'),__('Claire'),            
            __('Taylor'),__('Riley'),__('Camila'),__('Arianna'),__('Ashley'),        
            __('Brianna'),__('Sophie'),__('Peyton'),__('Bella'),__('Khloe'),        
            __('Genesis'),__('Alexa'),__('Serenity'),__('Kylie'),__('Aubree'),        
            __('Scarlett'),__('Stella'),__('Maya'),__('Katherine'),__('Julia'),     
            __('Lucy'),__('Madelyn'),__('Autumn'),__('Makayla'),__('Kayla'),            
            __('Mackenzie'),__('Lauren'),__('Gianna'),__('Ariana'),__('Faith'),        
            __('Alexandra'),__('Melanie'),__('Sydney'),__('Bailey'),__('Caroline'),        
            __('Naomi'),__('Morgan'),__('Kennedy'),__('Ellie'),__('Jasmine'),        
            __('Eva'),__('Skylar'),__('Kimberly'),__('Violet'),__('Molly'),    
            __('Aria'),__('Jocelyn'),__('Trinity'),__('London'),__('Lydia'),            
            __('Madeline'),__('Reagan'),__('Piper'),__('Andrea'),__('Annabelle'), 

            ]
        },
    
       
        'nordic': {
            'male': [__('Alf'), __('Warg'),__('Ingvar'),__('Rurik'),__('Ingolf'),
            __('Loki'),__('Odin'),__('Olaf'),__('Rendalf'),__('Rigvord'),
            __('Stain'),__('Thorboin'),__('Torgnir'),__('Hakon'),__('Erik'),
            __('Jarl'),__('Arne'),__('Alrik'),__('Alv'),__('Aud'),            
            __('Bard'),__('Brand'),__('Bjorn'),__('Bjarni'),__('Ingling'),        
            __('Oden'),__('Svenn'),__('Skald'),__('Thornbjorn'),__('Trognir'),        
            __('Ulf'),__('Ulwar'),__('Fenris'),__('Fridmund'),__('Hakon'),        
            __('Helgi'),__('Hrolfr'),__('Harald'),__('Hring'),__('Holm'),     
            ],

            'female': [__('Alva'),__('Alfhild'),__('Astrid'),__('Asgerd'),__('Iceveig'),
            __('Berta'),__('Brunhild'),__('Vandela'),__('Vigdis'),__('Gerda'),
            __('Gretta'),__('Ghudrun'),__('Ida'),__('Ingrid'),__('Isgerd'),
            __('Ingeborge'),__('Inga'),__('Isgerd'),__('Ragnild'),__('Ragngerd'),            
            __('Ranveig'),__('Rungerd'),__('Svanhild'),__('Sveya'),__('Seigrid'),        
            __('Sigun'),__('Solveig'),__('Torhild'),__('Freya'),__('Hanna'),        
            __('Helga'),__('Hild'),__('Ingrid'),__('Frigg'),__('Solgerd'),        
            ]
        },
    
        'oriental': {
            'male': [__('Kenshin'), __('Lu'),__('Bei'),__('Vei'),__('Gui'),
            __('Juang'),__('Jong'),__('Zen'),__('Giang'),__('Feng'),
            __('Akira'),__('Goro'),__('Jiro'),__('Ioshiro'),__('Ichiro'),
            __('Ken'),__('Koji'),__('Ketsuo'),__('Mamoru'),__('Shinji'),            
            __('Satoshi'),__('Takeshi'),__('Hideki'),__('Hiroshi'),__('Shin'),        
            ],
            'female': [__('Azumi'),__('Akiko'),__('Ayano'),__('Aoi'),__('Asuka'),
            __('Ayako'),__('Izumi'),__('Ioko'),__('Kaya'),__('Kumiko'),
            __('Kazumi'),__('Megumi'),__('Mizuki'),__('Miko'),__('Momoko'),
            __('Mariko'),__('Noriko'),__('Madoka'),__('May'),__('Nana'),            
            __('Naomi'),__('Netsumi'),__('Nori'),__('Rei'),__('Ren'),        
            __('Setsuko'),__('Sumiko'),__('Toshiko'),__('Fumiko'),__('Hitomi'),        
            __('Shizuko'),__('Uko'),__('Uri'),__('Jasuko'),__('Mei'),        
            __('Lin'),__('Iing'),__('Lui'),__('Mei'),__('Meifeng'),     
            ]
        },
    
        'african': {
            'male': [__('Abimba'), __('Bvanga'),__('Mamba'),__('Kimbo'),__('Tonga'),
            __('Changa'),__('Chakka'),__('Mbvanga'),__('Knegu'),__('Bubba'),
            __('Vakesa'),__('Jango'),__('Mandingo'),__('Zamba'),__('Kvaba'),
            __('Kavesi'),__('Nakoza'),__('Otingo'),__('Simba'),__('Tichanga'),            
            __('Unosi'),__('Baka'),__('Chima'),__('Chkuvema'),__('Obongo'),        
            ],
            
            'female': [__('Adana'),__('Akua'),__('Anyan'),__('Aching'),__('Gmenba'),
            __('Deonga'),__('Ezi'),__('Zeri'),__('Zema'),__('Imani'),
            __('Kleo'),__('Limuzi'),__('Mazozi'),__('Mirme'),__('Munash'),
            __('Ngozi'),__('Ndidi'),__('Nkiru'),__('Nsia'),__('Ojechi'),            
            __('Otabi'),__('Samanya'),__('Tinash'),__('Unati'),__('Eiku'),        
            ]
        },
    
        'native': {
            'male': [__('Aponvi'), __('Chingachguk'),__('Ahiga'),__('Achenu'),__('Vikho'),
            __('Isik'),__('Kangi'),__('Kvatho'),__('Keruk'),__('Kzekhochuk'),
            __('Kochat'),__('Kem'),__('Lepu'),__('Makhev'),__('Molimo'),
            __('Mechitziv'),__('Nashpeni'),__('Oglish'),__('Ohanzin'),__('Pejik'),            
            __('Kanhon'),__('Saik'),__('Sekihvo'),__('Sani'),__('Tenkshvoa'),        
            ],
            
            'female': [__('Loni'),__('Adsila'),__('Alameda'),__('Anpeitu'),__('Ayasha'),
            __('Belinge'),__('Vikishka'),__('Viteshna'),__('Vona'),__('Wuti'),
            __('Doli'),__('Ioki'),__('Isi'),__('Kvindok'),__('Kemerin'),
            __('Keliska'),__('Kesa'),__('Kesha'),__('Lilulai'),__('Lohmangoa'),            
            __('Makoi'),__('Mumitekh'),__('Mensi'),__('Naira'),__('Nijoni'),        
            __('Numis'),__('Nesha'),__('Oentia'),__('Orenda'),__('Pakhahontas'),        
            __('Pouka'),__('Raindi'),__('Soyala'),__('Siu'),__('Tipponi'),        
            ]
        },
    
        'arabic': {
            'male': [__('Abbas'), __('Abdula'),__('Abdul'),__('Abu'),__('Azamat'),
            __('Aziz'),__('Aidar'),__('Aman'),__('Ansar'),__('Arsen'),
            __('Ahmad'),__('Bagtrudin'),__('Bakhir'),__('Bulat'),__('Gafur'),
            __('Damir'),__('Daniyar'),__('Jambulat'),__('Jamil'),__('Jamal'),            
            __('Zakhir'),__('Zulfat'),__('Ibragim'),__('Ilnur'),__('Ilyas'),        
            __('Iskander'),__('Khasim'),__('Kharim'),__('Khemal'),__('Malik'),        
            __('Makhmud'),__('Mahdi'),__('Murad'),__('Murtaz'),__('Marat'),        
            __('Musrafa'),__('Muhammed'),__('Muhtar'),__('Nadir'),__('Nazif'),     
            __('Radik'),__('Ramadan'),__('Rasul'),__('Rafik'),__('Rulan'),            
            __('Rustam'),__('Said'),__('Sultan'),__('Sileiman'),__('Tamerlan'),        
            __('Umar'),__('Farid'),__('Hakim'),__('Gasan'),__('Shamil'),        
            __('Emir'),__('Yusuf'),__('Yasir'),__('Bashir'),__('Emil'),        
            ],
            'female': [__('Adiya'),__('Azara'),__('Azil'),__('Aziza'),__('Aida'),
            __('Aisha'),__('Amani'),__('Badiya'),__('Balkhis'),__('Bushra'),
            __('Galiya'),__('Gulya'),__('Gulchatai'),__('Chulpan'),__('Jamila'),
            __('Jabira'),__('Janna'),__('Juna'),__('Jukhra'),__('Izza'),            
            __('Isa'),__('Iffa'),__('Karima'),__('Lamia'),__('Leila'),        
            __('Farida'),__('Fatima'),__('Faina'),__('Udif'),__('Salomea'),        
            __('Ilmira'),__('Jasmin'),__('Naiya'),__('Gulfiya'),__('Nashida'),        
            ]
        },

        'TEMPLATE': {
            'male': [__(''), __(''),__(''),__(''),__(''),
            __(''),__(''),__(''),__(''),__(''),
            __(''),__(''),__(''),__(''),__(''),
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),    
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),      
            ],
            'female': [__(''),__(''),__(''),__(''),__(''),
            __(''),__(''),__(''),__(''),__(''),
            __(''),__(''),__(''),__(''),__(''),
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),    
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),     
            __(''),__(''),__(''),__(''),__(''),            
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),        
            __(''),__(''),__(''),__(''),__(''),      
            ]
        },
    
    }
