NUM_FIELDS = 8
NUM_SAMPLES = 51
URL_STEP = "https://votu.pe/presidential-steps/"
URL_RESULT = "https://votu.pe/presidential-results/grouped-by-compatibility"
FIELD_QUES = [4,7,4,3,4,3,5,4] # Number of questions per field
FIELD_PRIO = [5,1,4,8,7,3,6,2] # Priority of field. Field with priority 1 will appear first in every combination and so on
FIELD_ALTS = [[5,5,5,4],[5,4,5,4,5,3,3],[5,3,5,5],[5,5,5],[5,5,3,5],[3,6,4],[5,5,3,5,3],[3,4,4,3]] # Number of alternatives per field. The size of the list represents the number of questions given in FIELD_QUES

### Class names constants ###
FIELD_BTNS = "sc-bqyKva.ehfErK"
CONTINUE_BTN_1 = "sc-pFZIQ"
CONTINUE_BTN_2 = "sc-iqHYGH"
RADIO_BTNS = "sc-bqyKva.ehfErK"
CONTINUE_BTN_3 = "sc-bdfBwQ.gGYJmP"
PARTY_DIVS = "sc-bkzZxe.cSnsVU"
