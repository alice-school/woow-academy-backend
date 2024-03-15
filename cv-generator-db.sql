-- create database if not exists as psa
CREATE DATABASE IF NOT EXISTS psefop;

-- use the database
USE psefop;

--  Student and Recruiter Tables
CREATE TABLE
    Student (
        userID VARCHAR(50) NOT NULL,
        firstName VARCHAR(255) NOT NULL,
        lastName VARCHAR(255) NOT NULL,
        userName VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL,
        dob DATE NOT NULL,
        userPassword VARCHAR(255) NOT NULL,
        CONSTRAINT users_pk PRIMARY KEY (userID)
    );

update Student
set
    db = '1999-12-12'
where
    userID = '1';

INSERT INTO
    Address (
        addressID,
        userID,
        lineOne,
        lineTwo,
        city,
        postCode
    )
VALUES
    ('1', '1', '43/2', 'Gamagoda', 'Kalutara', '12016');

INSERT INTO
    CV_Profile (cvID, userID, profile_img, about, points)
VALUES
    (
        '1',
        'US2',
        'https://avatars.githubusercontent.com/u/50085447?v=4',
        'Developer | Tech enthusiast | Former Vice President @sliit-foss | Sub Dev Lead @ms-club-sliit | Student @vueschool | @mlsasrilanka (Alpha)',
        10
    );

-- insert student table rows
INSERT INTO
    Student (
        userID,
        firstName,
        lastName,
        userName,
        email,
        phone,
        dob,
        userPassword
    )
VALUES
    (
        '1',
        'Madhusha',
        'Prasad',
        'MadhushaPrasad',
        'madushaprasad@gmail.com',
        'pass123',
        '1999-12-12',
        '123456'
    );

CREATE TABLE
    Address (
        addressID VARCHAR(50) NOT NULL,
        userID VARCHAR(50) NOT NULL,
        lineOne VARCHAR(255) NOT NULL,
        lineTwo VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        postCode VARCHAR(255) NOT NULL,
        CONSTRAINT address_pk PRIMARY KEY (addressID),
        CONSTRAINT student_fk FOREIGN KEY (userID) REFERENCES Student (userID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert address table rows
INSERT INTO
    Address (
        addressID,
        userID,
        lineOne,
        lineTwo,
        city,
        postCode
    )
VALUES
    ('1', '1', '43/2', 'Gamagoda', 'Kalutara', '12016');

ALTER TABLE CV_Profile MODIFY COLUMN about VARCHAR(255) CHARACTER
SET
    utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE
    Recruiter (
        userID VARCHAR(50) NOT NULL,
        firstName VARCHAR(255) NOT NULL,
        lastName VARCHAR(255) NOT NULL,
        userName VARCHAR(255) NOT NULL,
        profile_img TEXT NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL,
        userPassword VARCHAR(255) NOT NULL,
        CONSTRAINT users_pk PRIMARY KEY (userID)
    );

-- insert recruiter table rows
INSERT INTO
    Recruiter (
        userID,
        firstName,
        lastName,
        userName,
        profile_img,
        email,
        phone,
        userPassword
    )
VALUES
    (
        '3',
        'Jane',
        'Doe',
        'jane_doe',
        'https://avatars.githubusercontent.com/u/50085447?v=4',
        'jh@gmail.com',
        '123456789',
        '123456'
    );

-- =====================================================================================================
-- cv profile section
CREATE TABLE
    CV_Profile (
        cvID VARCHAR(50) NOT NULL,
        userID VARCHAR(50) NOT NULL,
        profile_img TEXT NOT NULL,
        about LONGTEXT NOT NULL,
        points INT NOT NULL DEFAULT 'software developer',
        CONSTRAINT cv_profile_pk PRIMARY KEY (cvID),
        CONSTRAINT student_cv_fk FOREIGN KEY (userID) REFERENCES Student (userID) ON DELETE CASCADE ON UPDATE CASCADE
    );

ALTER TABLE CV_Profile MODIFY COLUMN about VARCHAR(255) CHARACTER
SET
    utf8mb4 COLLATE utf8mb4_unicode_ci;

update CV_Profile
set
    points = 10
where
    cvID = '1';

-- insert cv profile table rows
INSERT INTO
    CV_Profile (cvID, userID, profile_img, about, points)
VALUES
    (
        '1',
        '1',
        'https://avatars.githubusercontent.com/u/50085447?v=4',
        'Developer | Tech enthusiast | Former Vice President @sliit-foss | Sub Dev Lead @ms-club-sliit | Student @vueschool | @mlsasrilanka (Alpha)',
        10
    );

CREATE TABLE
    Objective (
        objectiveID VARCHAR(50) NOT NULL,
        cvID VARCHAR(50) NOT NULL,
        objective_description TEXT NOT NULL,
        CONSTRAINT objective_pk PRIMARY KEY (objectiveID),
        CONSTRAINT object_cv_fk FOREIGN KEY (cvID) REFERENCES CV_Profile (cvID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert objective table rows
INSERT INTO
    Objective (objectiveID, cvID, objective_description)
VALUES
    (
        'OBJ1',
        'CV8',
        'Developer | Tech enthusiast | Former Vice President @sliit-foss | Sub Dev Lead @ms-club-sliit | Student @vueschool | @mlsasrilanka (Alpha)'
    );

CREATE TABLE
    Education (
        educationID VARCHAR(50) NOT NULL,
        cvID VARCHAR(50) NOT NULL,
        institution VARCHAR(255) NOT NULL,
        education_course VARCHAR(255) NOT NULL,
        education_start_date DATE NOT NULL,
        education_end_date DATE NOT NULL,
        CONSTRAINT education_pk PRIMARY KEY (educationID),
        CONSTRAINT education_cv_fk FOREIGN KEY (cvID) REFERENCES CV_Profile (cvID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert education table rows
INSERT INTO
    Education (
        educationID,
        cvID,
        institution,
        education_course,
        education_start_date,
        education_end_date
    )
VALUES
    (
        'EDU1',
        'CV8',
        'SLIIT',
        'Software Engineering',
        '2020-01-01',
        '2024-01-01'
    );

CREATE TABLE
    Skill (
        skillID VARCHAR(50) NOT NULL,
        cvID VARCHAR(50) NOT NULL,
        skill_name VARCHAR(255) NOT NULL,
        skill_level VARCHAR(255) NOT NULL,
        CONSTRAINT skills_pk PRIMARY KEY (skillID),
        CONSTRAINT skill_cv_fk FOREIGN KEY (cvID) REFERENCES CV_Profile (cvID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert skill table rows
INSERT INTO
    Skill (skillID, cvID, skill_name, skill_level)
VALUES
    ('SK1', 'CV8', 'JavaScript', '100/10');

CREATE TABLE
    SocialMedia (
        socialMediaID VARCHAR(50) NOT NULL,
        cvID VARCHAR(50) NOT NULL,
        socialMedia_name VARCHAR(255) NOT NULL,
        socialMedia_link VARCHAR(255) NOT NULL,
        CONSTRAINT socialMedia_pk PRIMARY KEY (socialMediaID),
        CONSTRAINT social_media_cv_fk FOREIGN KEY (cvID) REFERENCES CV_Profile (cvID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert social media table rows
INSERT INTO
    SocialMedia (
        socialMediaID,
        cvID,
        socialMedia_name,
        socialMedia_link
    )
VALUES
    (
        'SM1',
        'CV1',
        'GitHub',
        'https://github.com/MadhushaPrasad'
    );

INSERT INTO
    SocialMedia (
        socialMediaID,
        cvID,
        socialMedia_name,
        socialMedia_link
    )
VALUES
    (
        'SM2',
        'CV1',
        'LinkedIn',
        'https://github.com/MadhushaPrasad'
    );

INSERT INTO
    SocialMedia (
        socialMediaID,
        cvID,
        socialMedia_name,
        socialMedia_link
    )
VALUES
    (
        'SM3',
        'CV1',
        'Stack Overflow',
        'https://github.com/MadhushaPrasad'
    );

CREATE TABLE
    WorkExperience (
        workExperienceID VARCHAR(50) NOT NULL,
        cvID VARCHAR(50) NOT NULL,
        company_name VARCHAR(255) NOT NULL,
        job_title VARCHAR(255) NOT NULL,
        job_start_date DATE NOT NULL,
        job_end_date DATE NOT NULL,
        job_description TEXT NOT NULL,
        job_address VARCHAR(255) NOT NULL,
        CONSTRAINT workExperience_pk PRIMARY KEY (workExperienceID),
        CONSTRAINT work_experience_cv_fk FOREIGN KEY (cvID) REFERENCES CV_Profile (cvID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert work experience table rows
INSERT INTO
    WorkExperience (
        workExperienceID,
        cvID,
        company_name,
        job_title,
        job_start_date,
        job_end_date,
        job_description,
        job_address
    )
VALUES
    (
        'WK1',
        'CV8',
        'Google',
        'Software Developer',
        '2018-12-01',
        '2022-6-01',
        'I am a software developer',
        'Nairobi'
    );

CREATE TABLE
    VolunteerExperience (
        volunteerExperienceID VARCHAR(50) NOT NULL,
        cvID VARCHAR(50) NOT NULL,
        organization_name VARCHAR(255) NOT NULL,
        role VARCHAR(255) NOT NULL,
        volunteer_start_date DATE NOT NULL,
        volunteer_end_date DATE NOT NULL,
        volunteer_description TEXT NOT NULL,
        CONSTRAINT volunteerExperience_pk PRIMARY KEY (volunteerExperienceID),
        CONSTRAINT volunteer_experience_cv_fk FOREIGN KEY (cvID) REFERENCES CV_Profile (cvID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert volunteer experience table rows
INSERT INTO
    VolunteerExperience (
        volunteerExperienceID,
        cvID,
        organization_name,
        role,
        volunteer_start_date,
        volunteer_end_date,
        volunteer_description
    )
VALUES
    (
        'VE1',
        'CV8',
        'Google',
        'Software Developer',
        '2018-01-01',
        '2022-01-01',
        'I am a software developer'
    );

CREATE TABLE
    Project (
        projectID VARCHAR(50) NOT NULL,
        cvID VARCHAR(50) NOT NULL,
        project_name VARCHAR(255) NOT NULL,
        project_description TEXT NOT NULL,
        CONSTRAINT project_pk PRIMARY KEY (projectID),
        CONSTRAINT project_cv_fk FOREIGN KEY (cvID) REFERENCES CV_Profile (cvID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert project table rows
INSERT INTO
    Project (
        projectID,
        cvID,
        project_name,
        project_description
    )
VALUES
    (
        'PJ1',
        'CV8',
        'Project 1',
        'I am a software developer'
    );

-- =====================================================================================================
-- Course section
CREATE TABLE
    Course (
        courseID VARCHAR(50) NOT NULL,
        course_thumbnail TEXT NOT NULL,
        course_name VARCHAR(255) NOT NULL,
        course_description TEXT NOT NULL,
        course_time DATE NOT NULL,
        course_keywords TEXT NOT NULL,
        CONSTRAINT course_pk PRIMARY KEY (courseID)
    );

-- insert course table rows
INSERT INTO
    Course (
        courseID,
        course_thumbnail,
        course_name,
        course_description,
        course_time,
        course_keywords
    )
VALUES
    (
        '1',
        'https://www.google.com',
        'Python',
        'Python is a programming language',
        '2022-01-01',
        'Python, Programming'
    );

CREATE TABLE
    Student_Course (
        student_courseID VARCHAR(50) NOT NULL,
        userID VARCHAR(50) NOT NULL,
        courseID VARCHAR(50) NOT NULL,
        course_status VARCHAR(255) NOT NULL,
        course_rate INT NOT NULL,
        course_view INT NOT NULL,
        perform_rate INT NOT NULL,
        CONSTRAINT student_course_pk PRIMARY KEY (userID, courseID),
        CONSTRAINT student_course_student_fk FOREIGN KEY (userID) REFERENCES Student (userID) ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT student_course_course_fk FOREIGN KEY (courseID) REFERENCES Course (courseID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- insert student course table rows
INSERT INTO
    Student_Course (
        student_courseID,
        userID,
        courseID,
        course_status,
        course_rate,
        course_view,
        perform_rate
    )
VALUES
    ('1', '1', '1', 'Completed', 5, 100, 5);

-- get student cv profile all data from the database that is the student, address, cv_profile, objective, education, skill, social_media, work_experience, volunteer_experience, project
SELECT
    Student.userID,
    Student.firstName,
    Student.lastName,
    Student.userName,
    Student.email,
    Student.phone,
    Student.dob,
    Student.userPassword,
    Address.addressID,
    Address.lineOne,
    Address.lineTwo,
    Address.city,
    Address.postCode,
    CV_Profile.cvID,
    CV_Profile.profile_img,
    CV_Profile.about,
    Objective.objectiveID,
    Objective.objective_description,
    Education.educationID,
    Education.institution,
    Education.education_course,
    Education.education_start_date,
    Education.education_end_date,
    Skill.skillID,
    Skill.skill_name,
    Skill.skill_level,
    SocialMedia.socialMediaID,
    SocialMedia.socialMedia_name,
    SocialMedia.socialMedia_link,
    WorkExperience.workExperienceID,
    WorkExperience.company_name,
    WorkExperience.job_title,
    WorkExperience.job_start_date,
    WorkExperience.job_end_date,
    WorkExperience.job_description,
    WorkExperience.job_address,
    VolunteerExperience.volunteerExperienceID,
    VolunteerExperience.organization_name,
    VolunteerExperience.role,
    VolunteerExperience.volunteer_start_date,
    VolunteerExperience.volunteer_end_date,
    VolunteerExperience.volunteer_description,
    Project.projectID,
    Project.project_name,
    Project.project_description
FROM
    Student
    JOIN Address ON Student.userID = Address.userID
    JOIN CV_Profile ON Student.userID = CV_Profile.userID
    JOIN Objective ON CV_Profile.cvID = Objective.cvID
    JOIN Education ON CV_Profile.cvID = Education.cvID
    JOIN Skill ON CV_Profile.cvID = Skill.cvID
    JOIN SocialMedia ON CV_Profile.cvID = SocialMedia.cvID
    JOIN WorkExperience ON CV_Profile.cvID = WorkExperience.cvID
    JOIN VolunteerExperience ON CV_Profile.cvID = VolunteerExperience.cvID
    JOIN Project ON CV_Profile.cvID = Project.cvID;

-- update   CV_Profile.profile_img, in  CV_Profile table
UPDATE CV_Profile
SET
    profile_img = 'https://avatars.githubusercontent.com/u/137147492?v=4'
WHERE
    CV_Profile.cvID = '1';