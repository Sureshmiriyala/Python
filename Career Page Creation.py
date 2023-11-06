class CareerPortal:
    def __init__(self):
        self.jobs = []
        self.applications = []

    def add_job_post(self, job_post):
        self.jobs.append(job_post)

    def get_number_of_applications(self):
        return len(self.applications)


class Admin:
    def __init__(self, career_portal):
        self.career_portal = career_portal

    def add_job_post(self, job_post):
        self.career_portal.add_job_post(job_post)

    def get_number_of_applications(self):
        return self.career_portal.get_number_of_applications()

    def view_application_details(self):
        return self.career_portal.applications


class User:
    def __init__(self, career_portal):
        self.career_portal = career_portal

    def get_number_of_jobs(self):
        return len(self.career_portal.jobs)

    def apply_for_job(self, job_post):
        self.career_portal.applications.append(job_post)


if __name__ == '__main__':
    career_page = CareerPortal()
    admin = Admin(career_page)
    user = User(career_page)

    admin.add_job_post("Job Post 1")
    admin.add_job_post("Job Post 2")

    user.apply_for_job("Job Post 1")
    user.apply_for_job("Job Post 2")

    print("Number of jobs:", user.get_number_of_jobs())
    print("Number of applications:", admin.get_number_of_applications())
    print("Application details:", admin.view_application_details())
