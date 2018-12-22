# Data Science in the Cloud

These are the notebooks for the talk I gave on "Data Science in the Cloud" as part of KU IT Meet 2018.

The session was structured with case studies corresponding to the decreasing level of control you have over the underlying resources.

- Local Computer / EC2 Instances: [Intro to Data Science](intro-data-science) 
- AWS Sagemaker: [Detect digits in cheque](amount-in-cheque)
- AWS ML Services: [CCTV Weapon Detection](weapon-detection-aws) 
- Serverless Computing: [Customer Reviews Sentiment](review-sentiments)
- Client Side ML: [Person Presence Detection](client-side-ml)

### Questions from Audience
- What approach would you recommend to beginners for learning machine learning?  
    > Learn using top-down approach rather than bottom-up. I personally feel [fast.ai](https://www.fast.ai) is the best course to start with.
    
- What's the difference between Google Colaboratory and AWS Sagemaker Notebooks? What advantage does AWS Sagemaker offer?
    > Google Colaboratory is a free notebook service offered by Google. It provides **Tesla K80** GPU runtime but it's shared among users. The CPU, RAM and GPU capacity provided is fixed.  
    AWS Sagemaker is a paid service by Amazon that hosts jupyter notebooks. You can choose an [instance type](https://aws.amazon.com/sagemaker/pricing/instance-types/) as per your usecase. The CPU, RAM and GPU capacity are flexible. 
