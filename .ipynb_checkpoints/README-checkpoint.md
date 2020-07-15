# DSI Capstone - Jared Delora-Ellefson

### Problem Statement:  
Identify conspiracy trends in the political discussions occurring on Reddit between Jan 2016 and Dec 2016. This period covers the 11 months leading up to the election of Donald Trump as US President, and one month after.

**The fundamental question to be answered: Did the conspiracies that plagued the 2016 begin with chatter on social media? How much growth in the amount of chatter on Reddit was due to political figures and misinformation websites tweeting about them?**


### Aproach
**There are four conspiracy theories popular during the election that have been proven to be false. These are:**  
- Seth Rich Murder
- Pizzagate + John Podesta Pedophilia Accusations
- Hillary Clinton Mishandling of classified materials
- BlueLivesMatter (Originating in 2014 but according to the Robert Mueller investigation this topic was pushed by Russian Intelligence to sew division amoung the American population)  

[Dissecting Trump's Most Rabid Online Following](https://fivethirtyeight.com/features/dissecting-trumps-most-rabid-online-following/)  
FiveThirtyEight.com has done some work looking at Reddit behavior surrounding Donald Trump. In the above article a number of subreddits are identified as being particularly toxic along with the reasons.  
    
    
[Online Political Discourse in the Trump Era, RISHAB NITHYANAND et al](https://arxiv.org/pdf/1711.05303.pdf)    
  
The above paper is a study of incivility in discourse before and after the 2016 US presidential election. The header, in part:  

**"We identify general trends in the (in)civility and complexity of political discussions occurring on Reddit between January 2007 and
May 2017 – a period spanning both terms of Barack Obama’s presidency and the first 100 days of Donald Trump’s presidency."**

This paper used a number of models, including a spaCy entity recognition model to investigate trends in civil discourse. This paper identifies a number of subreddits whose rhetoric grew particularly incivil.
  
**These subreddits have been shown to spread misinformation and to have discussed the conspiracies noted above:**  
- r/the_donald
- r/Republican
- r/Conservative
- r/uncensorednews
- r/TheRedPill

**These five subreddits will be used for the investigation since they have already been identified as particularly uncivil during the election.**


Twitter handles associated with misinformation, known to have discussed the conspiracies identified above:  
- @realdonaldtrump  
- @realrogerstone1  
- @donaldtrumpjr   
- @BreitbartNews   
- @infowarsmedia  
- @zerohedge

All of these twitter handles have been shown to have engaged in spreading the conspiracies noted above.

### The Data

The data used for this analysis was taken from Reddit. Every comment made at r/the_donald for the 2016 was collected.

### Data Processing

<img src="./images/DataProcessing.png" alt="doggo" width="1000"/>


### Prodigy Training
The NLP training tool Podigy was used to traint the spaCy models. NER was performed using seed words. All entities relevant to the custom label CON were labeled using prodigy, then a model was generated. This model takes a string and then returns any entities detected in the string. The strings used in this analysis were comments from r/the_donald and the terms being identified are terms related to the conspiracies we're searching for.

### Model Metrics

<img src="./images/metrics.png" alt="doggo" width="1000"/>

### Preliminary Results on the Seth Rich Conspiracy

<img src="./images/results.png" alt="doggo" width="1000"/>

### Next Steps
1. Complete Seth Rich Analysis Reddsit Analysis.
2. Complete Reddit Analysis for the other identified conspiracies.
3. Use the NER model to analyze the twitter accounts listed above.
4. Exploratory Analysis and Correlation Findings

## Directory
```bash
.
├── README.md
├── DSI_Capstone_Presentation.pdf
├── misc_files
├── data
│   ├── ent_counts
│   │   ├── ents_1.csv
│   │   ├── ents_2.csv
│   │   ├── ents_3.csv
│   │   ├── ents_4.csv
│   │   ├── ents_5.csv
│   │   ├── ents_6.csv
│   │   ├── ents_7.csv
│   │   ├── ents_8.csv
│   │   ├── ents_9.csv
│   │   ├── ents_10.csv
│   │   ├── ents_11.csv
│   │   ├── ents_12.csv
│   │   ├── Kmeans_Result.ipynb
│   │   ├── trials/
│   │   └── w2v_trial.ipynb
│   ├── trumptweets.csv
└── spacy
    ├── TextManager.py (primary text cleaner / spaCy model runner)
    ├── EntExplorer.py
    ├── ent_dataframes
    │   ├── jan_seth_rich_ents
    │   ├── feb_seth_rich_ents
    │   ├── mar_seth_rich_ents
    │   ├── apr_seth_rich_ents
    │   ├── may_seth_rich_ents
    │   ├── jun_seth_rich_ents
    │   ├── jul_seth_rich_ents
    │   ├── aug_seth_rich_ents
    │   ├── sep_seth_rich_ents
    │   ├── oct_seth_rich_ents
    │   ├── nov_seth_rich_ents
    │   └── dec_seth_rich_ents
    ├── the_donald
    │   └── files: Not_included_in_repo (comments taken from r/the_donald at Reddit)
    ├── training_data
    │   └── files: Not_included_in_repo
    ├── donald_model
    │   └── spaCy model: Not_included_in_repo
    └── CON_patters.jsonl (spaCy NER patterns)


```
