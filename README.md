# 👋 Hi, I'm Zhengyang Xu

📧 Email: [fy1999xu@gmail.com](mailto:fy1999xu@gmail.com)  
🐙 GitHub: [Younger330](https://github.com/Younger330)  
📚 Google Scholar: [Zhengyang Xu](https://scholar.google.com/citations?user=c-PDzPEAAAAJ&hl=en)  

---

## 🎓 Education

**Northwest University**, Xi’an, China  
*Master of Computer Science* (09/2022 – present)  
GPA: **3.53** (Top 30%)  
- Courses: English Academic Paper Writing, Machine Learning, Multiscale Image Analysis, Multimodal Image Analysis  
- Scholarships: China National Scholarship, Second Prize (2022/23), Third Prize (2023/24, 2024/25)

**Guilin University of Electronic Technology**, Guilin, China  
*Bachelor of Applied Statistics* (09/2017 – 06/2021)  
GPA: **3.12** (Top 25%)  
- Courses: Mathematical Analysis, Data Structures, Python Big Data Analysis  

---

## 🔬 Research Interests

Medical images · Weak supervision · Foundation models · Multimodal models · Unsupervised learning  

---

## 📄 Publications

1. **Li, Hansheng**, **Xu, Zhengyang** *(equal first authorship)* et al.  
   *Segment Membranes and Nuclei from Histopathological Images via Nuclei Point-Level Supervision*.  
   *MICCAI 2023*, pp. 539–548.

2. **Xu, Zhengyang**, et al.  
   *Addressing Sparse Annotation: A Novel Semantic Energy Loss for Tumor Cell Detection from Histopathologic Images*.  
   *IEEE BIBM 2023*, pp. 1588–1595.

3. **Xu, Zhengyang**, et al.  
   *Robust Prototype-based Multi-class Cell Detection via Sparse-Annotated Histological Images*.  
   *(To be submitted to IEEE Transactions on Medical Imaging)*

4. **Li, Hansheng**, **Xu, Zhengyang** *(equal first authorship)* et al.  
   *PathUniDet: A Universal Framework for Scalable and Efficient Pathological Image Detection Across Diverse Tasks and Modalities*.  
   *(Under review at Nature Machine Intelligence)*

---

## 🧪 Projects

### 🔹 Point-based Cell Membranes and Nuclei Segmentation (09/2022–01/2023)  [[code link]](https://github.com/Lion-shine/Segment-Membranes-and-Nuclei-from-Histopathological-Images-via-Nuclei-Point-level-Supervision) 
*Core Member (Master Dissertation)*  
- Proposed a novel point-based cell membrane segmentation method, which can signiﬁcantly reduce the cost of pixel-level annotation required in conventional methods.
- This is the ﬁrst study that uses point-level supervision for membrane segmentation from IHC images and also the ﬁrst to employ point annotations to supervise the segmentation of two objects simultaneously.
- Extensive experiments conﬁrm the efﬁcacy of the proposed method, attaining performance comparable to models trained with fully supervised data.
- Achieved performance comparable to fully supervised models, published at *MICCAI 2023*.

### 🔹 Sparse Annotation Cell Detection (01/2023–present)  [[code link]](https://github.com/Younger330/SemanticEnergyLoss) 
*Project Leader (Master Dissertation)*  
- I identified that incomplete feature distribution learned only from sparse annotations hinders the model’s ability to localize unannotated cells and first propose a multi-class sparse cell detection method.
- Exhaustive experiments have achieved SOTA performance via both sparse and exhaustive annotations, showing a mean 0.24 performance enhancement over fully supervised methods. This indicates that this method can replace fully supervised methods across all levels of clinical annotation quality.
- Single-class version published at *IEEE BIBM 2023*, multi-class version being submitted to *TMI*.

### 🔹 Universal Pathology Detection Framework (09/2023–present)
*Project Leader (Master Dissertation)*  
- Proposed a universal detection and segmentation method for pathological images using a simple network as the primary framework, capable of performing multi-category, multi-level analysis tasks. It outperforms single-task models by a mean F1 score of 0.078 and surpasses the SOTA universal model by 0.164. 
- The process only requires specifying the current task type to dynamically perform task-relevant analyses, including tumor region segmentation, tissue region segmentation, cell segmentation, and cell keypoint detection.
-  A single consumer-grade GPU can deploy this model, further facilitating the implementation and application of related intelligent diagnostic algorithms.
- *Submitted to Nature Machine Intelligence.*

### 🔹 Breast Cancer Virtual IHC Generation (06/2024–present) [[code link]](https://github.com/Younger330/Virtual-IHC-Generation) 
*Project Leader*  
- Developed a method to generate IHC-stained whole-slide images (WSIs) from H&E-stained slides for early tumor region identification and immunohistochemical analysis, including CK56 (membrane staining), P63 (nuclear staining), and CK7 (membrane staining).
- Performed slide registration using Valis, enhanced alignment through color deconvolution and quality filtering, and subsequently applied CycleGAN for image generation.
- Clinically oriented project developed with clinical doctors, delivering results aligned with medical expectations.


### 🔹 Bone Marrow Cell Classification (07/2023–05/2024)
*Core Member*  
- Employed YOLOv9 to detect 43 classes of Bone Marrow cells derived from both internal and external validation datasets. 
- Utilized the Copy-Paste data augmentation to address the scarcity of detectable cells in each image and implemented the Reinhard algorithm to address the significant style variations in external validation datasets.


---

## 💡 Skills

- **Languages**: English (IELTS 6.5), Chinese (Native)
- **Programming**: Python (PyTorch, OpenCV, Matplotlib, NumPy), Matlab  
- **Tools**: Git, LaTeX

---

*Thanks for visiting my GitHub! Feel free to connect with me via email or explore my projects.*
