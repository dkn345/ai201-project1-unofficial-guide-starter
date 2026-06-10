# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
I am choosing CS professor at UTD domain since there is a lot of information to compare with such as UTDGrades and trends. There is also rate my professor and reddits. Since there are many resources, it is easier to paint a better picture for the user and consolidate it. It is difficult through official channels since they can be biased, so using the student created tools and experiences is the best way to share perspectives.
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 |UTDGrades|Shows the grades and ratings of professors at UTD (this is one specific UTD prof) 1337 |https://www.utdgrades.com/results?search=CS+1337&sectionId=24518|
| 2 |UTD Grades|Shows the grades and ratings of professors at UTD (this is one specific UTD prof) different 1337 professor |https://www.utdgrades.com/results?search=CS+1337&sectionId=52085 |
| 3 |UTD Trends |Shows the grades and ratings of professors at UTD (this is for a course) 3354 |https://trends.utdnebula.com/dashboard?searchTerms=CS+3354&availability=26F|
| 4 |UTD Trends |Shows the grades and ratings of professors at UTD (this is for a course) 4391 |https://trends.utdnebula.com/dashboard?searchTerms=CS+4391&availability=26F|
| 5 |Reddit |UTD Thread |https://www.reddit.com/r/utdallas/comments/tzuzbm/best_cs_professors/ |
| 6 |Reddit |UTD Thread a different one |https://www.reddit.com/r/utdallas/comments/1sfeu7k/advice_on_cs_3341_cs_2336_and_cs_2340_professors/ |
| 7 |Coursicle |A specific UTD Professor in this link |https://www.coursicle.com/utdallas/professors/Simeon+Ntafos/ |
| 8 |Coursicle |A different UTD Professor |https://www.coursicle.com/utdallas/professors/Gopal+Gupta/ |
| 9 |Rate My Professor |Ratings and review about a CS UTD Prof |https://www.ratemyprofessors.com/professor/1833058 |
| 10|Rate My Professor |Ratings and review about a CS UTD Prof |https://www.ratemyprofessors.com/professor/1554657 |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 250

**Overlap:** 25

**Why these choices fit your documents:** I am choosing around 250 characters because a lot of the sources have only around couple sentences. Some have longer but the majority has smaller amounts, so 250 characters is a good choice. I choose overlap of 25 because the characters and posts are relatively small but having some overlap could help, so I chose a relatively small size.

STRETCH: I compared chunk sizes such as 350-400 and overlap around 25-50. I noticed that increasing chunk and overlap did not help much since the sources are short, so my distances were higher yielding less relevant chunks. The initial choice of 250 and 25 is what I stuck with since there were some results with less distances and more accurate answers.

**Final chunk count:** 64

Example Chunks: 
[Coursicle1.txt] (dist: 0.381) Source: Coursicle
URL: https://www.coursicle.com/utdallas/professors/Simeon+Ntaf...
[Reddit2.txt] (dist: 0.660) or Simeon Ntafos.
Avoid Nhut Nguyen.
Take Alice Wang for CS 2340. She is helpful...
[RateMyProfessor2.txt] (dist: 0.718) Source: Rate My Professor
URL: https://www.ratemyprofessors.com/professor/155465...
[Reddit1.txt] (dist: 0.733) at even after missing many lectures, one office-hours session with Elmer Salazar...
[Reddit2.txt] (dist: 0.742) r Stats whose name is not Octavius Smiley. He is one of the best professors at U...
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2 via sentence-transformers due to the simplicity and light weight nature of this model.

**Production tradeoff reflection:** I would choose accuracy and latency to improve performance but also sort of adjust chunking approaches depending on the source since some sources are going to be shorter than others. Accuracy would be the biggest thing and I would try to incorporate semantic search and various chunking strategies for different documents. Latency is important for getting fast results so that would be another main thing I would focus on. 

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** The model is instructed to answer only from retrieved context. In "generator.py", the prompt says: "Answer using ONLY the provided context. If the answer is not contained in the context, say: 'I don't have enough information on that.'" The system message also says: "Answer only from retrieved documents."

**How source attribution is surfaced in the response:** The source attribution is returned in the retrieved section of the Gradio UI. They are collected via program and returned in the UI. This helps with verification of responses through the sources.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 |Who is the best teacher for CS 2340? |Alice Wang |Alice Wang |Partially Relevant |Accurate |
| 2 |How is Gopal Gupta's teaching style? |Okay around |No information |Partially relevant |Inaccurate |
| 3 |Who is the best CS professor? |Klyne Smith, Jason Smith |Klyne Smith, Jason Smith |Relevant |Partially Accurate |
| 4 |How is Simeon Ntafos? |Negative views |Negative views |Relevant |Accurate |
| 5 |What are the grades for 3354 like? |A/A- |No information |Partially relevant |Inaccurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:** How is Gopal Gupta's teaching style?

**What the system returned:** I don't have enough information on that.

**Root cause (tied to a specific pipeline stage):** The relevant information was too small and although the sources retrieved were somewhat relevant, since there was not enough information the retrieval suffered. Since the retrieval was not good (noisy information for instance), the generation suffered which returned no information. 

**What you would change to fix it:** Having more information, scraping would be one method since the sources were not that many. In addition, I believe semantic chunking could have helped along with more targeted chunking sizes because the retrieval did not return anything, so slight variation could have been beneficial.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** The spec helped me have a roadmap of what to do. In addition, I paid attention to details even more such as chunk sizes and why I am making those decisions. This helped me move forward quicker since I had a plan and be intentional with my decision making. 

**One way your implementation diverged from the spec, and why:** One way I diverged from the spec is chunk sizes. I spent a good portion of the time testing chunk sizes such as 400/350 and overlap such as 30/40. I wanted to see if I could get more context. However, the original plan of 250 characters and 25 overlap worked better since it worked overall. 

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* I gave AI the chunking strategy and asked to help implement the function.
- *What it produced:* It produced starter chunking code using a character-based chunking strategy with approximately 200-character chunks and 25-character overlap.
- *What I changed or overrode:* I tried that and felt it was not returning enough important information, so I changed to 250 and kept the overlap. 

**Instance 2**

- *What I gave the AI:* I gave project pipeline image and checking my retrieval approach.
- *What it produced:* It produced starter code for ChromaDB retrieval, embeddings with all-MiniLM-L6-v2, and the retrieval function that returned the top-k chunks.
- *What I changed or overrode:* I experimented with different N-Result/top k and settled for 5 even tho it gave 10 as the code since it showed more relevant results.
