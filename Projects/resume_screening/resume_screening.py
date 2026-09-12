import os
import re
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
RESUME_FOLDER="resumes"
JD_FILE="jd_samples.txt"
SKILLS_LIST=[
    'python','java','c++','sql','machine learning','deep learning','nlp','data analysis','excel','communincation','tensorflow','pytorch',
    'html','css','javascript','react','django','flask','aws','power bi','tableau','git','linux','r programming','data structures','oop','pandas','numpy','teamwork','leadership'
]
EDUCATION_LIST=[
    'btech','be','mtech','mba','mca',
    'bca','bsc','msc','phd','bachelor','master','diploma'
]
def extract_text_from_pdf(file_path):
    """reads a pdf file and returns all the text inside it as one string"""
    text=""
    reader=PyPDF2.PdfReader(file_path)
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text=text+page_text+""
    return text
def clean_text(text):
    """lowercase everything and remove extra symbols/spaces"""
    text=text.lower()
    text=text.replace('.','')
    text=re.sub(r'[^a-z0-9\s+]',' ',text)
    text=re.sub(r'\s+',' ',text)
    return text.strip()
def find_skills(text):
    found=[]
    for skill in SKILLS_LIST:
        if skill in text:
            found.append(skill)
    return found
def find_education(text):
    found=[]
    for edu in EDUCATION_LIST:
        if edu in text:
            found.append(edu)
    return found
def find_experience_years(text):
    """
    looks for patterns like '3 years' or 5+ years experiene' and return the highest number it finds
    """
    matches=re.findall(r'(\d+)\+?\s*years',text)
    if len(matches)==0:
        return 0
    years=[int(m) for m in matches]
    return max(years)
def calculate_match_score(jd_text,resume_text):
    """
    Uses TF-IDF to convert both texts into vectors, thrn checks cosine similarity between them.Return a percentage score.
    """
    documents=[jd_text,resume_text]
    vectorizer= TfidfVectorizer(stop_words='english')
    tfidf_matrix=vectorizer.fit_transform(documents)
    similarity=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])
    score=similarity[0][0]*100
    return round(score,2)
def main():
    print("=== AI Resume Screening System===")
    print()
    jd_input=input("Paste the job description here(or press enter to use jd_sample.txt):")
    if jd_input.strip()=="":
        if not os.path.exists(JD_FILE):
            print(f"Could not find{JD_FILE}.Please create it or pate a job description.")
            return
        with open(JD_FILE,"r",encoding="utf-8") as f:
            jd_input=f.read()
    jd_clean=clean_text(jd_input) 
    jd_skills=find_skills(jd_clean)
    print()
    print("Skills detected in JOb Description:",jd_skills)
    print()
    if not os.path.isdir(RESUME_FOLDER):
        print(f"Folder '{RESUME_FOLDER}' not found.Create it and put resume PDFs in side.") 
        return
    pdf_files=[f for f in os.listdir(RESUME_FOLDER) if f.lower().endswith(".pdf")]
    if len(pdf_files)==0:
        print(f"No PDF files found inside '{RESUME_FOLDER}' folder.")
        return
    results=[]
    for file_name in pdf_files:
        print("Processing resume:",file_name)
        full_path=os.path.join(RESUME_FOLDER,file_name)
        raw_text= extract_text_from_pdf(full_path)    
        if raw_text.strip()=="":
            print(" ->could not extract any text from this file,skipping") 
            continue
        clean_resume=clean_text(raw_text)
        resume_skills=find_skills(clean_resume)
        resume_education=find_education(clean_resume)
        experience_years=find_experience_years(clean_resume)
        match_score=calculate_match_score(jd_clean,clean_resume)
        common_skills=list(set(jd_skills)&set(resume_skills))
        results.append({
            "Candidate":file_name,
            "Match Score (%)":match_score,
            "Matched Skills":",".join(common_skills) if common_skills else "None",
            "All Skills Found":",".join(resume_skills)if resume_skills else "None",
            "Education":",".join(resume_education) if resume_education else "Not mentioned",
            "Experience (years)": experience_years
        })
    if len(results)==0:
        print("No resumes could be processed.")
        return
    df=pd.DataFrame(results)
    df=df.sort_values(by="Match Score (%)",ascending=False)
    df.reset_index(drop=True,inplace=True)
    df.index=df.index +1
    print()
    print("----- Final Candidate Ranking-----")
    print(df.to_string())
    output_file="resume_ranking_output.csv"
    df.to_csv(output_file,index=True)
    print()
    print("Results saved to",output_file)
if __name__=="__main__":
    main()