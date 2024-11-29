# japan-dofj-pr-extractor
Extracts all press releases from the Japanese DoFJ's archives between the years 2005-2024.

Focuses specifically on extracting press releases with Korea included in the title, but can be used for researching other trends with other countries if the code is adjusted.
When opening the xlsx file, please be sure to set your Excel to be able to read Japanese or else you won't be able to read the press articles.

**FUTURE STEPS:**
I want to fix this code so I can use it moving on in the future to look more in-depth at the articles posted rather than just focus on Korea, but for the scope of this current project its a bit unrealistic to have this step ready.

- Make code for archiving the 2017-2005 articles cleaner. (It currently runs on O(n^3) which is highly inefficient)
- Get a list of all countries with the following data: Country name (Japanese), Country name abbreviations (Japanese), Country name (English)
- Use above list to go through all of the press releases. 

**POSSIBLE FUTURE DIRECTIONs:**
- Make code go through each press release *article* rather than just the title itself
- Possibly find a way to summarize the article information with some sort of LLM to assist with the qualitative research portion.
