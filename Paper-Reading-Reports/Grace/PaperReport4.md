# A Formal Security Analysis of the W3C Web Payment APIs: Attacks and Verification

## Introduction
Both comsumers and merchants rely on third party apps to make and collect payments online. However, because of these numerous methods of payment, this may negatively effect user experience or leave more opportunity for security breaches. Therefore, the W3C has implemented a method to integrate payment as a native functionality into a browser. In this study, researchers found two sources of previously unknown vulnerabilities to this method, as well as two proposed solutions.

## Discovered Vulnerabilities
The first attack has to do with the retry mechanism built into the WPA (step 13). During a payment, if incorrect information is entered, the merchant will allow the user to retry inputting the information and state its reasons. However, during a potential attack, a malicious merchant can inspect the information and delcare it to be incorrect, even though it may be perfectly valid, and ask the user to choose a different payment handler. On th Web Payment API, it would look as if it were a normal error message, and a user will consequently pay twice, essentially being double charged. Since the merchant has the control to display any error message, they can perform any attack without detection because it would be indistinguishable from a legitimate flow from a the perspective of the API.

<img width="427" alt="image" src="https://user-images.githubusercontent.com/73855373/178325771-8ec6ca47-f305-4f9f-ada7-0d66b46141e2.png">

The second possible attack arises from ambiguous payment method data. A malicious merchant may create a payment request with two entries that have the exact same payment method identifiers. However, one could have no processing fees while the other may have a high amount. The customer, who cannot see the difference, may randomly choose the option with no fee. However, during a Payment Request Event, the handler also cannot cannot see the difference since it is only given the two identical identifiers. Therefore, to break ties it could choose randomly and may choose the option with the high processing fee, therefore charging the customer extra without their knowledge.

<img width="427" alt="image" src="https://user-images.githubusercontent.com/73855373/178330631-293a7368-719d-43cc-bef7-d25cbe7d8c0d.png">

## Proposed Solutions
For the first aforementioned attack, the payment handler may include a "status", meaning that a payment has already been paid, the status will change and prevent the browser from allowing the user to change handlers. For the second attack, a fix could be made so that the browser could simply reject possible ambiguous entries such as the one mentioned before.

## Takeaways/Conclusions
The paper, although simple, discovered new vulnerabilities that could affect a signficant proces on the web. Their proposed solutions were suggested to the W3C, who implemented their fixes. They were not only able to find these insecurities, but used dummy processes in order to verify these vulnerabilities. 
