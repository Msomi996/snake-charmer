
# Import requests so Python can send a request to a website.
import requests

# Import BeautifulSoup so Python can read and search the website's HTML.
from bs4 import BeautifulSoup

# Import urlparse to separate a URL into parts, including its domain.
from urllib.parse import urlparse

# Store the website URL supplied by the applicant.
website_url = "https://signupmerchant.capitecbank.co.za/"

# Store the business name declared by the applicant (sample data).
applicant_business_name = "Capitec Bank"

# Store the contact email declared by the applicant (sample data).
applicant_email = "example@capitecbank.co.za"

# Send a request to retrieve the website's HTML, with a 15-second timeout.
try:
    response = requests.get(website_url, timeout=15)

    # Stop processing if the website returns an unsuccessful HTTP status.
    response.raise_for_status()

    # Convert the returned HTML into a structure we can search.
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the page title, if the website provides one.
    page_title = soup.title.get_text(strip=True) if soup.title else ""

    # Extract the visible text from the page's main heading, if one exists.
    main_heading = soup.find("h1").get_text(" ", strip=True) if soup.find("h1") else ""

    # Extract all visible text from the page into one string.
    page_text = soup.get_text(" ", strip=True)

    # Find email-like strings in the visible text and mailto links.
    import re  # Import regular expressions to search for email patterns.
    emails = set(re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", page_text))

    # Look for links that explicitly use a mailto: email address.
    for link in soup.find_all("a", href=True):
        if link["href"].startswith("mailto:"):
            # Remove the mailto: prefix and any query string from the address.
            email = link["href"][7:].split("?")[0]

            # Add the email to the set so duplicate addresses are avoided.
            if email:
                emails.add(email)

    # Extract the domain from the submitted website URL.
    website_domain = urlparse(website_url).hostname or ""

    # Remove a leading www. so common domain formats are easier to compare.
    website_domain = website_domain.removeprefix("www.")

    # Check whether the declared business name appears in the page text.
    business_name_found = (
        applicant_business_name.casefold() in page_text.casefold()
    )

    # Check whether the applicant's email domain matches the website domain.
    applicant_email_domain = applicant_email.rsplit("@", 1)[-1].lower()

    # This is a simple comparison, not proof that the applicant controls either.
    email_domain_matches = applicant_email_domain == website_domain.lower()

    # Print the information extracted from the website.
    print("\n--- WEBSITE INFORMATION ---")
    print("Website:", website_url)
    print("Domain:", website_domain)
    print("Page title:", page_title or "Not found")
    print("Main heading:", main_heading or "Not found")
    print("Emails found:", sorted(emails) if emails else "None found")

    # Print the comparison results for the onboarding review.
    print("\n--- VERIFICATION CHECKS ---")
    print("Declared business name found:", business_name_found)
    print("Applicant email domain matches website:", email_domain_matches)

    # Flag the case if either basic comparison raises a concern.
    if not business_name_found or not email_domain_matches:
        print("\nOutcome: REFER FOR REVIEW")
        print("Reason: One or more checks did not match.")
    else:
        # A match is only a preliminary signal, not proof of legitimacy.
        print("\nOutcome: BASIC CHECKS MATCH")
        print("Further verification is still required.")

# Handle common request errors without crashing with a long traceback.
except requests.RequestException as error:
    # Tell the user that the website could not be retrieved successfully.
    print("Could not retrieve the website:", error)
