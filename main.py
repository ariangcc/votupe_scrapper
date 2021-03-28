#!/usr/bin/env python

"""
	main.py
	-------
	This module contains the main function calls for the votu.pe webpage scrapping.
"""

__author__ = "Arian Gallardo"

from constants import FIELD_ALTS, FIELD_PRIO, FIELD_QUES
from constants import URL_STEP, NUM_FIELDS, NUM_SAMPLES
from constants import FIELD_BTNS, CONTINUE_BTN_1, CONTINUE_BTN_2, RADIO_BTNS, CONTINUE_BTN_3
from utils import get_combs, generate_masks, click_elements, get_parties_info
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def run_scrapping(driver):
	""" Initializes and run web scrapping routines to obtain information about
		 parties and their possible scores, according to the votu.pe questionary.
		 Runs in a randomized manner: check get_combs con ./utils.py for further 
		 information.

		 :type driver: WebDriver
		 :param driver: Web Driver for Mozilla Firefox.

	"""

	driver.get(URL_STEP + "1")

	itrs = 1
	d = {}

	for idxs in generate_masks(NUM_FIELDS):
		questions_cnt = FIELD_ALTS[idxs[0]] + FIELD_ALTS[idxs[1]] + FIELD_ALTS[idxs[2]]
	
		for comb in get_combs(questions_cnt):
			driver.get(URL_STEP + "1")
			click_elements(web_driver=driver, class_name=FIELD_BTNS, idxs=idxs)
			click_elements(web_driver=driver, class_name=CONTINUE_BTN_1)

			driver.get(URL_STEP + "2")	
			click_elements(web_driver=driver, class_name=CONTINUE_BTN_2)

			driver.get(URL_STEP + "3")
			comb_pos = 0

			for field_idx in idxs:
				for _ in range(FIELD_QUES[field_idx]):
					click_elements(web_driver=driver, class_name=RADIO_BTNS, idxs=[comb[comb_pos]])
					comb_pos += 1
					click_elements(web_driver=driver, class_name=CONTINUE_BTN_3)

			party_names, scores = get_parties_info(driver)

			for idx, name in enumerate(party_names):
				d[name] = d.get(name,0) + scores[idx]
		
			print("Iteración #{}".format(str(itrs)))
			itrs += 1
			print(d)


	total_score = 0

	for e in d:
		total_score += d.get(e)
	
	lst = []

	for e in d:
		lst.append((d.get(e)*100/total_score, e))
	
	lst = sorted(lst)[::-1]

	for e in lst:
		print("{} -> {}".format(e[1], str(e[0])))


if __name__ == "__main__":
	driver = webdriver.Firefox()
	run_scrapping(driver)
	driver.close()
