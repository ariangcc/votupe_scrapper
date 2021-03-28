#!/usr/bin/env python

"""
	utils.py
	--------
	This module implements functions that help on the web scrapping task.
"""

__author__ = "Arian Gallardo"

import random
from time import sleep
from constants import NUM_SAMPLES, FIELD_PRIO, PARTY_DIVS, URL_RESULT

def get_combs(questions_cnt):
	""" Yields random combinations for each alternative given on the
		 questions_cnt list. Depends on the constant NUM_SAMPLES.

		 :type questions_cnt: list
		 :param questions_cnt: Count of alternatives per question.

	"""
	n, total_combs = len(questions_cnt), 1

	for num_ques in questions_cnt:
		total_combs *= num_ques
	
	rand_idxs = []

	for _ in range(min(NUM_SAMPLES, total_combs)):
		rand_idx = random.randint(0,total_combs)
		
		while rand_idx in rand_idxs:
			rand_idx = random.randint(0,total)
		rand_idxs.append(rand_idx)
	
	rand_idxs = sorted(rand_idxs)

	for idx in rand_idxs:
		comb, accum, suffix_prod = [], 0, total_combs
		
		for i in range(n):
			suffix_prod //= questions_cnt[i]
			pos = 0
			while accum + pos * suffix_prod <= idx:
				pos += 1
			pos -= 1
			accum += pos * suffix_prod
			comb.append(pos)

		yield comb

def generate_masks(num_fields):
	""" Yields combinations of 3 indexes out of num_fields to pick
		 a set of topics to answer.

		 :type num_fields: int
		 :param num_fields: Number of fields
		
	"""
	for msk in range(256):
		cur_msk, pos = msk, 0
		idxs = []
		while cur_msk > 0:
			if cur_msk % 2 != 0:
				idxs.append(pos)
			pos += 1
			cur_msk //= 2
		
		if len(idxs) != 3:
			continue

		for i in range(3):
			for j in range(i+1,3):
				if FIELD_PRIO[idxs[i]] > FIELD_PRIO[idxs[j]]:
					idxs[i], idxs[j] = idxs[j], idxs[i]

		yield idxs

def click_elements(web_driver, class_name, idxs = None):
	""" Click elements that match with class_name. If idxs
		 is None, clicks only the first.

		 :type web_driver: WebDriver
		 :param web_driver: Web Driver for Mozilla Firefox

		 :type class_name: str
		 :param class_name: Class name to match

		 :type idxs: list | None
		 :param idxs: If not None, list of indexes of elements to click
	"""
	elements = None
	
	while True:
		try:
			elements = web_driver.find_elements_by_class_name(class_name)
			if len(elements) == 0:
				raise Exception
			break
		except Exception as e:
			continue

	if idxs:
		for idx in idxs:
			elements[idx].click()
	else:
		elements[0].click()

def get_parties_info(web_driver):
	""" Returns parties info from the results page.

		 :type web_driver: WebDriver
		 :param web_driver: Web Driver for Mozilla Firefox
	"""
	web_driver.get(URL_RESULT)
	elements = None
	sleep(3)

	while True:
		try:
			elements = web_driver.find_elements_by_class_name(PARTY_DIVS)
			if len(elements) == 0:
				raise Exception
			break
		except Exception as e:
			continue
	
	party_names = [x.text for x in elements[::2]]
	scores = [int(x.text[:x.text.find('%')]) for x in elements[1::2]]

	return party_names, scores

