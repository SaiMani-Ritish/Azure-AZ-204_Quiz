import streamlit as st

# Define the quiz questions, options, correct answers, and explanations.
# These questions are extracted from the provided AZ-204 exam dumps.
quiz_questions = [
    {
        "question": "You use Azure Table storage to store customer information for an application. The data contains customer details and is partitioned by last name. You need to create a query that returns all customers with the last name Smith. Which code segment should you use?",
        "options": [
            "A. TableQuery.Generate FilterCondition(\"PartitionKey\", Equals, \"Smith\")",
            "B. TableQuery. Generate FilterCondition(\"LastName\", Equals, \"Smith\")",
            "C. TableQuery.Generate FilterCondition(\"PartitionKey\", Query Comparisons. Equal, \"Smith\")",
            "D. TableQuery Generate FilterCondition(\"LastName\", QueryComparisons. Equal, \"Smith\")"
        ],
        "correct_answer": "C",
        "explanation": "To retrieve all entities in a partition with PartitionKey=\"Smith\", the correct code segment is 'TableQuery.Generate FilterCondition(\"PartitionKey\", QueryComparisons. Equal, \"Smith\")'."
    },
    {
        "question": "You are developing a project management service by using ASP.NET. The service hosts conversations, files, to-do lists, and a calendar that users can interact with at any time. The application uses Azure Search for allowing users to search for keywords in the project data. You need to implement code that creates the object which is used to create indexes in the Azure Search service. Which object(s) should you use?",
        "options": [
            "A. Search Service",
            "B. SearchIndexClient",
            "C. SearchServiceClient",
            "D. SearchCredentials",
            "E. B and C"
        ],
        "correct_answer": "E",
        "explanation": "The client libraries for Azure Search define classes like SearchServiceClient and SearchIndexClient for operations related to the search service and indexes respectively. Both are used for creating and managing indexes."
    },
    {
        "question": "You are developing a solution that will use Azure messaging services. You need to ensure that the solution uses a publish-subscribe model and eliminates the need for constant polling. What are two possible ways to achieve the goal?",
        "options": [
            "A. Service Bus",
            "B. Event Hub",
            "C. Event Grid",
            "D. Queue",
            "E. A and C"
        ],
        "correct_answer": "E",
        "explanation": "For a publish-subscribe model that eliminates constant polling, Azure Service Bus and Azure Event Grid are recommended. Service Bus is suitable for high-value enterprise messaging, while Event Grid provides event-driven architecture for reacting to state changes."
    },
    {
        "question": "You develop a serverless application using several Azure Functions. These functions connect to data from within the code. You want to configure tracing for an Azure Function App project. You need to change configuration settings in the host.json file. Which tool should you use?",
        "options": [
            "A. Azure portal",
            "B. Azure PowerShell",
            "C. Azure Functions Core Tools (Azure CLI)",
            "D. Visual Studio"
        ],
        "correct_answer": "A",
        "explanation": "The host.json file, which contains runtime-specific configurations for an Azure Function App, can be directly updated using the function editor built into the Azure portal."
    },
    {
        "question": "You are writing code to create and run an Azure Batch job. You have created a pool of compute nodes. You need to choose the right class and its method to submit a batch job to the Batch service. Which method should you use?",
        "options": [
            "A. JobOperations.CreateJob()",
            "B. CloudJob.Enable (IEnumerable<BatchClientBehavior>)",
            "C. CloudJob.CommitAsync(IEnumerable<BatchClientBehavior>, CancellationToken)",
            "D. JobOperations.EnableJob(String, IEnumerable<BatchClientBehavior>)",
            "E. JobOperations. Enable JobAsync(Strin)",
            "F. IEnumerable<BatchClientBehavior>. CancellationToken)"
        ],
        "correct_answer": "C",
        "explanation": "After creating a `CloudJob` object using `BatchClient.JobOperations.CreateJob`, the `Commit` method (or `CommitAsync` for asynchronous operations) is used to submit the job to the Batch service."
    },
    {
        "question": "You develop Azure solutions. You must connect to a No-SQL globally-distributed database by using the .NET API. You need to create an object to configure and execute requests in the database. Which code segment should you use?",
        "options": [
            "A. new Container(EndpointUri, PrimaryKey);",
            "B. new Database(Endpoint, PrimaryKey);",
            "C. new CosmosClient(EndpointUri, PrimaryKey);"
        ],
        "correct_answer": "C",
        "explanation": "To connect to an Azure Cosmos DB (No-SQL globally-distributed database) using the .NET API and create an object for configuring and executing requests, you should use the `CosmosClient` class. Example: `new CosmosClient(EndpointUri, PrimaryKey)`."
    },
    {
        "question": "You are developing an Azure Cosmos DB solution by using the Azure Cosmos DB SQL API. The data includes millions of documents. Each document may contain hundreds of properties. The properties of the documents do not contain distinct values for partitioning. Azure Cosmos DB must scale individual containers in the database to meet the performance needs of the application by spreading the workload evenly across all partitions over time. You need to select a partition key. Which two partition keys can you use?",
        "options": [
            "A. a concatenation of multiple property values with a random suffix appended",
            "B. a single property value that does not appear frequently in the documents",
            "C. a hash suffix appended to a property value",
            "D. a value containing the collection name",
            "E. A and C"
        ],
        "correct_answer": "E",
        "explanation": "To ensure even workload distribution across partitions in Azure Cosmos DB when distinct values are not naturally present, you can use synthetic partition keys formed by concatenating multiple property values or by appending a random or hash suffix to a property value. This allows for parallel write operations across partitions."
    },
    {
        "question": "A company is developing a solution that allows smart refrigerators to send temperature information to a central location. You have an existing Service Bus. The solution must receive and store messages until they can be processed. You create an Azure Service Bus instance by providing a name, pricing tier, subscription, resource group, and location. You need to complete the configuration. Which Azure CLI or PowerShell command should you run?",
        "options": [
            "A. az servicebus namespace create -resource-group fridge-rg -name fridge-ns -location fridge-loc",
            "B. az servicebus queue create --resource-group fridge-rg --namespace-name fridge-ns --name fridge-q",
            "C. connectionString=\$(az servicebus namespace authorization-rule keys list --resource-group fridge-rg --fridge-ns fridge-ns --name RootManageSharedAccessKey --query primaryConnectionString --output tsv)",
            "D. az group create --name fridge -rg --location fridge-log"
        ],
        "correct_answer": "B",
        "explanation": "Since a Service Bus instance (namespace) has already been created, the next step to enable message reception and storage is to create a Service Bus queue within that namespace. The command `az servicebus queue create` is used for this purpose."
    },
    {
        "question": "You are developing an ASP.NET Core Web API web service. The web service uses Azure Application Insights for all telemetry and dependency tracking. The web service reads and writes data to a database other than Microsoft SQL Server. You need to ensure that dependency tracking works for calls to the third-party database. Which two Dependency Telemetry properties should you store in the database?",
        "options": [
            "A. Telemetry.Context. Operation.Id",
            "B. Tetemetry. Context.Cloud.RoleInstance",
            "C. Telemetry.Id",
            "D. Telemetry.ContextSession.Id",
            "E. Telemetry.Name",
            "F. A and C"
        ],
        "correct_answer": "F",
        "explanation": "For custom operations tracking and ensuring dependency tracking works for calls to third-party databases with Application Insights, `Telemetry.Context.Operation.Id` and `Telemetry.Id` are typically used to correlate operations and dependencies."
    },
    {
        "question": "You develop and deploy a Java RESTful API to Azure App Service. You open a browser and navigate to the URL for the API. You receive the following error message: Failed to load http://api: No 'Access- Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost: 6000' is therefore not allowed access You need to resolve the error. What should you do?",
        "options": [
            "A. Bind an SSL certificate",
            "B. Enable authentication",
            "C. Enable CORS",
            "D. Map a custom domain",
            "E. Add a CDN"
        ],
        "correct_answer": "C",
        "explanation": "The 'Access-Control-Allow-Origin' header missing error indicates a Cross-Origin Resource Sharing (CORS) issue. To resolve this, you need to enable CORS for your API in Azure App Service, allowing requests from specified origins."
    },
    {
        "question": "You need to resolve the Shipping web site error. How should you configure the Azure Table Storage service?",
        "options": [
            "A. Box 1: AllowedOrigins, Box 2: http://test-shippingapi.wideworldimporters.com, Box 3: Allowed Origins, Box 4: POST",
            "B. Box 1: ExposedHeaders, Box 2: http://test-shippingapi.wideworldimporters.com, Box 3: Allowed Headers, Box 4: GET",
            "C. Box 1: AllowedMethods, Box 2: http://www.wideworldimporters.com, Box 3: Exposed Headers, Box 4: PUT",
            "D. Box 1: Allowed Origins, Box 2: http://wideworldimporters.com, Box 3: Allowed Methods, Box 4: HEAD"
        ],
        "correct_answer": "A",
        "explanation": "The error 'No 'Access-Control-Allow-Origin' header is present on the requested resource' indicates a CORS issue. You need to configure `AllowedOrigins` to include `http://test-shippingapi.wideworldimporters.com` and specify `POST` as an `AllowedMethod` if POST requests are being made."
    },
    {
        "question": "You need to migrate on-premises shipping data to Azure. What should you use?",
        "options": [
            "A. Azure Migrate",
            "B. Azure Cosmos DB Data Migration tool (dt.exe)",
            "C. AzCopy",
            "D. Azure Database Migration service"
        ],
        "correct_answer": "D",
        "explanation": "For migrating MongoDB data from on-premises to Azure Cosmos DB with minimal downtime, Azure Database Migration Service is the recommended tool."
    },
    {
        "question": "You need to support the requirements for the Shipping Logic App. What should you use?",
        "options": [
            "A. Azure Active Directory Application Proxy",
            "B. Point-to-Site (P2S) VPN connection",
            "C. Site-to-Site (S2S) VPN connection",
            "D. On-premises Data Gateway"
        ],
        "correct_answer": "D",
        "explanation": "To connect to on-premises data sources from Azure Logic Apps, you should use the on-premises data gateway. It acts as a bridge for secure data transfer."
    },
    {
        "question": "A company is developing a Java web app. The web app code is hosted in a GitHub repository located at https://github.com/Contoso/webapp. The web app must be evaluated before it is moved to production. You must deploy the initial code release to a deployment slot named staging. You need to create the web app and deploy the code. How should you complete the commands?",
        "options": [
            "A. az group create, az appservice plan create, az webapp create, az webapp deployment slot create, az webapp deployment source config",
            "B. az webapp create, az group create, az appservice plan create, az webapp deployment slot create, az webapp deployment source config",
            "C. az appservice plan create, az webapp create, az group create, az webapp deployment slot create, az webapp deployment source config",
            "D. az webapp deployment slot create, az group create, az appservice plan create, az webapp create, az webapp deployment source config"
        ],
        "correct_answer": "A",
        "explanation": "The correct sequence for creating and deploying a web app with a deployment slot via Azure CLI is: create resource group, create app service plan, create web app, create deployment slot, then configure deployment source."
    },
    {
        "question": "You are developing an app that manages users for a video game. You plan to store the region, email address, and phone number for the player. Some players may not have a phone number. The player's region will be used to load-balance data. Data for the app must be stored in Azure Table Storage. You need to develop code to retrieve data for an individual player. How should you complete the code?",
        "options": [
            "A. Box 1: region, Box 2: email, Box 3: CloudTable, Box 4: TableOperation query =.., Box 5: TableResult",
            "B. Box 1: email, Box 2: region, Box 3: CloudTableClient, Box 4: TableEntity query =.., Box 5: TableEntity",
            "C. Box 1: phone, Box 2: region, Box 3: TableEntity, Box 4: TableQuery query =.., Box 5: TableResultSegment",
            "D. Box 1: region, Box 2: phone, Box 3: CloudTable, Box 4: TableResult query =.., Box 5: TableOperation"
        ],
        "correct_answer": "A",
        "explanation": "For retrieving an individual player's data from Azure Table Storage, the `PartitionKey` should be the `region` (for load balancing) and the `RowKey` should be a unique identifier like `email`. The operations involve `CloudTable` and `TableOperation` to get a `TableResult`."
    },
    {
        "question": "You are preparing to deploy a medical records application to an Azure virtual machine (VM). The application will be deployed by using a VHD produced by an on-premises build server. You need to ensure that both the application and related data are encrypted during and after deployment to Azure. Which three actions should you perform in sequence?",
        "options": [
            "A. Encrypt the on-premises VHD by using BitLocker without a TPM. Upload the VM to Azure Storage. Run the Azure PowerShell command Set-AzureRMVMOSDisk. Run the Azure PowerShell command Set-AzureRmVMDiskEncryptionExtension.",
            "B. Encrypt the on-premises VHD by using BitLocker with a TPM. Upload the VM to Azure Storage. Run the Azure PowerShell command New-AzureRmVM. Run the Azure PowerShell command Set-AzureRmVMDiskEncryptionExtension.",
            "C. Upload the VHD to Azure Storage. Run the Azure PowerShell command Set-AzureRmVMOSDisk. Run the Azure PowerShell command Set-AzureRmVMDiskEncryptionExtension.",
            "D. Run the Azure PowerShell command Set-AzureRmVMOSDisk. Encrypt the on-premises VHD by using BitLocker without a TPM. Upload the VM to Azure Storage. Run the Azure PowerShell command Set-AzureRmVMDiskEncryptionExtension."
        ],
        "correct_answer": "A",
        "explanation": "The correct sequence for encrypting a VM with a VHD from on-premises involves encrypting the VHD locally (without TPM for VMs), uploading it to Azure Storage, then using PowerShell commands `Set-AzureRMVMOSDisk` and `Set-AzureRmVMDiskEncryptionExtension` to configure the OS disk and enable disk encryption on the Azure VM."
    },
    {
        "question": "You are a developer for a software as a service (SaaS) company that uses an Azure Function to process orders. The Azure Function currently runs on an Azure Function app that is triggered by an Azure Storage queue. You are preparing to migrate the Azure Function to Kubernetes using Kubernetes-based Event Driven Autoscaling (KEDA). You need to configure Kubernetes Custom Resource Definitions (CRD) for the Azure Function. Which CRDs should you configure?",
        "options": [
            "A. Deployment, ScaledObject, Secret",
            "B. Deployment, TriggerAuthentication, Secret",
            "C. ScaledObject, Secret, Azure Function code",
            "D. Deployment, Polling interval, Azure Storage connection string"
        ],
        "correct_answer": "A",
        "explanation": "When deploying Azure Functions to Kubernetes with KEDA, you typically configure `Deployment` for the function code, `ScaledObject` for autoscaling based on events (like queue messages), and `Secret` to store sensitive information such as connection strings."
    },
    {
        "question": "Fourth Coffee has an ASP.NET Core web app that runs in Docker. The app is mapped to the www.fourthcoffee.com domain. Fourth Coffee is migrating this application to Azure. You need to provision an App Service Web App to host this docker image and map the custom domain to the App Service web app. A resource group named Fourth Coffee Public WebResource Group has been created in the WestUS region that contains an App Service Plan named AppServiceLinuxDockerPlan. Which order should the CLI commands be used to develop the solution?",
        "options": [
            "A. #/bin/bash, az webapp create, az webapp config container set, az webapp config hostname add",
            "B. az webapp create, #/bin/bash, az webapp config container set, az webapp config hostname add",
            "C. az webapp config hostname add, az webapp create, az webapp config container set, #/bin/bash",
            "D. #/bin/bash, az webapp config hostname add, az webapp create, az webapp config container set"
        ],
        "correct_answer": "A",
        "explanation": "The correct order to provision an App Service Web App for Docker and map a custom domain involves first setting up variables, then creating the web app, configuring its container image, and finally adding the custom hostname."
    },
    {
        "question": "You develop a website. You plan to host the website in Azure. You expect the website to experience high traffic volumes after it is published. You must ensure that the website remains available and responsive while minimizing cost. You need to deploy the website. What should you do?",
        "options": [
            "A. Deploy the website to an App Service that uses the Shared service tier",
            "B. Configure the App Service plan to automatically scale when the CPU load is high.",
            "C. Deploy the website to a virtual machine and configure a Scale Set to increase the virtual machine instance count when the CPU load is high.",
            "D. Deploy the website to an App Service that uses the Standard service tier and configure the App Service plan to automatically scale when the CPU load is high."
        ],
        "correct_answer": "D",
        "explanation": "For high traffic volumes, availability, responsiveness, and cost minimization, deploying to an App Service with a Standard tier (or higher, like Premium or Isolated) and configuring auto-scaling based on CPU load is the most appropriate solution. Shared tier is not suitable for high traffic."
    },
    {
        "question": "You are developing a new page for a website that uses Azure Cosmos DB for data storage. The feature uses documents that have the following format: You must display data for the new page in a specific order. You create the following query for the page: You need to configure a Cosmos DB policy to the support the query. How should you configure the policy?",
        "options": [
            "A. Box 1: compositeIndexes, Box 2: descending",
            "B. Box 1: includedPaths, Box 2: ascending",
            "C. Box 1: excludedPaths, Box 2: descending",
            "D. Box 1: indexingMode, Box 2: ascending"
        ],
        "correct_answer": "A",
        "explanation": "To support queries that order by multiple properties in Azure Cosmos DB, you need to define a `compositeIndex` in your indexing policy. The `order` property within the composite index specifies the sort order, e.g., `descending`."
    },
    {
        "question": "You are developing an ASP.NET Core Web API web service. The web service uses Azure Application Insights for all telemetry and dependency tracking. The web service reads and writes data to a database other than Microsoft SQL Server. You need to ensure that dependency tracking works for calls to the third-party database. Which two Dependency Telemetry properties should you store in the database?",
        "options": [
            "A. Telemetry.Context. Operation.Id",
            "B. Tetemetry. Context.Cloud.RoleInstance",
            "C. Telemetry.Id",
            "D. Telemetry.ContextSession.Id",
            "E. Telemetry.Name",
            "F. A and C"
        ],
        "correct_answer": "F",
        "explanation": "For custom operations tracking and ensuring dependency tracking works for calls to third-party databases with Application Insights, `Telemetry.Context.Operation.Id` and `Telemetry.Id` are typically used to correlate operations and dependencies."
    },
    {
        "question": "You need to support the message processing for the ocean transport workflow. Which four actions should you perform in sequence?",
        "options": [
            "A. Create an integration account in the Azure portal. Link the Logic App to the integration account. Add partners, schemas, certificates, maps, and agreements. Create a custom connector for the Logic App.",
            "B. Link the Logic App to the integration account. Create an integration account in the Azure portal. Add partners, schemas, certificates, maps, and agreements. Create a custom connector for the Logic App.",
            "C. Create a custom connector for the Logic App. Create an integration account in the Azure portal. Link the Logic App to the integration account. Add partners, schemas, certificates, maps, and agreements.",
            "D. Add partners, schemas, certificates, maps, and agreements. Link the Logic App to the integration account. Create an integration account in the Azure portal. Create a custom connector for the Logic App."
        ],
        "correct_answer": "A",
        "explanation": "The standard sequence for setting up an integration account with Logic Apps for B2B scenarios is: create the integration account, link the Logic App to it, add the necessary artifacts (partners, schemas, etc.), and then create custom connectors as needed."
    },
    {
        "question": "You need to configure Azure CDN for the Shipping web site. Which configuration options should you use?",
        "options": [
            "A. Tier: Standard, Profile: Akamai, Optimization: dynamic site acceleration",
            "B. Tier: Premium, Profile: Microsoft, Optimization: general web delivery",
            "C. Tier: Standard, Profile: Microsoft, Optimization: large file download",
            "D. Tier: Premium, Profile: Akamai, Optimization: video-on-demand media streaming"
        ],
        "correct_answer": "A",
        "explanation": "For maximizing performance of dynamic content and minimizing latency/costs, `Dynamic Site Acceleration (DSA)` is the key optimization, which is available with Azure CDN Standard from Akamai or Verizon profiles. Standard tier is a suitable starting point."
    },
    {
        "question": "You need to secure the Shipping Function app. How should you configure the app?",
        "options": [
            "A. Authorization level: Function, User claims: JSON Web Token (JWT), Trigger type: HTTP",
            "B. Authorization level: Anonymous, User claims: Shared Access Signature (SAS) token, Trigger type: HTTP",
            "C. Authorization level: Admin, User claims: API Key, Trigger type: queue",
            "D. Authorization level: User, User claims: JSON Web Token (JWT), Trigger type: blob"
        ],
        "correct_answer": "A",
        "explanation": "To implement secure function endpoints with Azure AD, typically you'd use 'Function' authorization level, rely on 'JSON Web Token (JWT)' for user claims from Azure AD, and use 'HTTP' as the trigger type for web app integration."
    },
    {
        "question": "You are developing an Azure Function App by using Visual Studio. The app will process orders input by an Azure Web App. The web app places the order information into Azure Queue Storage. You need to review the Azure Function App code shown below. NOTE: Each correct selection is worth one point.",
        "options": [
            "A. The code will log the time that the order was processed from the queue: No. When the ProcessOrders function fails, the function will retry up to five times for a given order, including the first try: Yes. When there are multiple orders in the queue, a batch of orders will be retrieved from the queue and the ProcessOrders function will run multiple instances concurrently to process the orders: Yes. The ProcessOrders function will output the order to an Orders table in Azure Table Storage: Yes.",
            "B. The code will log the time that the order was processed from the queue: Yes. When the ProcessOrders function fails, the function will retry up to five times for a given order, including the first try: No. When there are multiple orders in the queue, a batch of orders will be retrieved from the queue and the ProcessOrders function will run multiple instances concurrently to process the orders: No. The ProcessOrders function will output the order to an Orders table in Azure Table Storage: No.",
            "C. The code will log the time that the order was processed from the queue: No. When the ProcessOrders function fails, the function will retry up to five times for a given order, including the first try: Yes. When there are multiple orders in the queue, a batch of orders will be retrieved from the queue and the ProcessOrders function will run multiple instances concurrently to process the orders: No. The ProcessOrders function will output the order to an Orders table in Azure Table Storage: Yes.",
            "D. The code will log the time that the order was processed from the queue: Yes. When the ProcessOrders function fails, the function will retry up to five times for a given order, including the first try: Yes. When there are multiple orders in the queue, a batch of orders will be retrieved from the queue and the ProcessOrders function will run multiple instances concurrently to process the orders: Yes. The ProcessOrders function will output the order to an Orders table in Azure Table Storage: No."
        ],
        "correct_answer": "A",
        "explanation": "Based on standard Azure Functions queue trigger behavior: Insertion Time is logged, not processing time. `maxDequeueCount` controls retries (default 5). Queue triggers process batches concurrently. Output bindings can direct data to Azure Table Storage."
    },
    {
        "question": "You must ensure that the external party cannot access the data in the SSN column of the Person table. Will each protection method meet the requirement?",
        "options": [
            "A. Enable AlwaysOn encryption: Yes. Set the column encryption setting to disabled: No. Assign users to the Public fixed database role: Yes. Store column encryption keys in the system catalog view in the database: No.",
            "B. Enable AlwaysOn encryption: No. Set the column encryption setting to disabled: Yes. Assign users to the Public fixed database role: No. Store column encryption keys in the system catalog view in the database: Yes.",
            "C. Enable AlwaysOn encryption: Yes. Set the column encryption setting to disabled: Yes. Assign users to the Public fixed database role: No. Store column encryption keys in the system catalog view in the database: No.",
            "D. Enable AlwaysOn encryption: No. Set the column encryption setting to disabled: No. Assign users to the Public fixed database role: Yes. Store column encryption keys in the system catalog view in the database: Yes."
        ],
        "correct_answer": "A",
        "explanation": "Always Encrypted can protect sensitive data like SSN. Disabling encryption would expose it. Assigning users to the Public role usually doesn't grant access to encrypted data without explicit permissions. Keys should be stored securely, e.g., in Key Vault, not in system catalog views."
    },
    {
        "question": "You are creating a script that will run a large workload on an Azure Batch pool. Resources will be reused and do not need to be cleaned up after use. You have the following parameters: You need to write an Azure CLI script that will create the jobs, tasks, and the pool. In which order should you arrange the commands to develop the solution?",
        "options": [
            "A. az batch pool create, az batch job create, az batch task create, for i in (1..$numberOfJobs) do",
            "B. az batch job create, az batch pool create, az batch task create, for i in (1..$numberOfJobs) do",
            "C. az batch task create, az batch job create, az batch pool create, for i in (1..$numberOfJobs) do",
            "D. for i in (1..$numberOfJobs) do, az batch pool create, az batch job create, az batch task create"
        ],
        "correct_answer": "A",
        "explanation": "To set up Azure Batch, you first create a pool of compute nodes, then a job to manage tasks, add individual tasks to the job, and finally, if needed, loop to add multiple tasks or jobs."
    },
    {
        "question": "Margie's Travel is an international travel and bookings management service. The company is expanding into restaurant bookings. You are tasked with implementing Azure Search for the restaurants listed in their solution. You create the index in Azure Search. You need to import the restaurant data into the Azure Search service by using the Azure Search .NET SDK. Solution: 1. Create a SearchIndexClient object to connect to the search index.. 2. Create a DataContainer that contains the documents which must be added. 3. Create a DataSource instance and set its Container property to the DataContainer. 4. Call the Documents. Suggest method of the SearchIndexClient and pass the DataSource. Does the solution meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "correct_answer": "B",
        "explanation": "The correct method for importing documents into an Azure Search index using the .NET SDK is to create an `IndexBatch` containing the documents and then call the `Documents.Index` method of the `SearchIndexClient`, not `Documents.Suggest`."
    },
    {
        "question": "You develop an app that allows users to upload photos and videos to Azure storage. The app uses a storage REST API call to upload the media to a blob storage account named Account1. You have blob storage containers named Container1 and Container2. Uploading of videos occurs on an irregular basis. You need to copy specific blobs from Container1 to Container2 in real time when specific requirements are met, excluding backup blob copies. What should you do?",
        "options": [
            "A. Download the blob to a virtual machine and then upload the blob to Container2.",
            "B. Run the Azure PowerShell command Start-AzureStorageBlobCopy.",
            "C. Copy blobs to Container2 by using the Put Blob operation of the Blob Service REST API.",
            "D. Use AzCopy with the Snapshot switch blobs to Container2."
        ],
        "correct_answer": "B",
        "explanation": "The `Start-AzureStorageBlobCopy` PowerShell cmdlet is the most straightforward and efficient way to copy blobs between containers in Azure Storage, especially for real-time scenarios, as it offloads the copy operation to the storage service itself."
    },
    {
        "question": "You are a developer for a SaaS company that offers many web services. All web services for the company must meet the following requirements: Use API Management to access the services Use OpenID Connect for authentication Prevent anonymous usage A recent security audit found that several web services can be called without any authentication. Which API Management policy should you implement?",
        "options": [
            "A. jsonp",
            "B. authentication-certificate",
            "C. check-header",
            "D. validate-jwt"
        ],
        "correct_answer": "D",
        "explanation": "To prevent anonymous usage and enforce authentication with OpenID Connect for an API Management service, the `validate-jwt` policy is used to validate the incoming JWT tokens."
    },
    {
        "question": "You are developing an Azure solution to collect point-of-sale (POS) device data from 2,000 stores located throughout the world. A single device can produce 2 megabytes (MB) of data every 24 hours. Each store location has one to five devices that send data. You must store the device data in Azure Blob storage. Device data must be correlated based on a device identifier. Additional stores are expected to open in the future. You need to implement a solution to receive the device data. Solution: Provision an Azure Service Bus. Configure a topic to receive the device data by using a correlation filter. Does the solution meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "correct_answer": "A",
        "explanation": "Azure Service Bus topics support publish-subscribe messaging and correlation filters, which can be used to efficiently receive and correlate device data, making it a suitable solution for this scenario."
    },
    {
        "question": "You are developing an Azure solution to collect point-of-sale (POS) device data from 2,000 stores located throughout the world. A single device can produce 2 megabytes (MB) of data every 24 hours. Each store location has one to five devices that send data. You must store the device data in Azure Blob storage. Device data must be correlated based on a device identifier. Additional stores are expected to open in the future. You need to implement a solution to receive the device data. Solution: Provision an Azure Notification Hub. Register all devices with the hub. Does the solution meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "correct_answer": "B",
        "explanation": "Azure Notification Hubs are primarily for sending push notifications to mobile devices, not for collecting and storing large volumes of device data for correlation. Azure Service Bus or Event Hubs would be more appropriate for data ingestion."
    },
    {
        "question": "You are implementing a software as a service (SaaS) ASP.NET Core web service that will run as an Azure Web App. The web service will use an on-premises SQL Server database for storage. The web service also includes a WebJob that processes data updates. Four customers will use the web service. Each instance of the WebJob processes data for a single customer and must run as a singleton instance. Each deployment must be tested by using deployment slots prior to serving production data. Azure costs must be minimized. Azure resources must be located in an isolated network. You need to configure the App Service plan for the Web App. How should you configure the App Service plan?",
        "options": [
            "A. Number of VM instances: 4, Pricing tier: Isolated",
            "B. Number of VM instances: 2, Pricing tier: Standard",
            "C. Number of VM instances: 8, Pricing tier: Premium",
            "D. Number of VM instances: 16, Pricing tier: Consumption"
        ],
        "correct_answer": "A",
        "explanation": "For singleton WebJobs, deployment slots for testing, and isolated network resources, the 'Isolated' pricing tier is required as it provides a dedicated App Service Environment (ASE). The number of VM instances can be scaled as needed, with 4 being a reasonable starting point."
    },
    {
        "question": "You are building a website to access project data related to terms within your organization. The website does not allow anonymous access. Authentication performed using an Azure Active Directory (Azure AD) app named internal. The website has the following authentication requirements: Azure AD users must be able to login to the website. Personalization of the website must be based on membership in Active Directory groups. You need to configure the application's manifest to meet the authentication requirements. How should you configure the manifest?",
        "options": [
            "A. groupMembershipClaims: All, oauth2Permissions: delegated",
            "B. optionalClaims: groupMembershipClaims, oauth2Permissions: allowPublicClient",
            "C. groupMembershipClaims: SecurityGroup, oauth2Permissions: requiredResourceAccess",
            "D. optionalClaims: User.Read, oauth2Permissions: oauth2AllowImplicitFlow"
        ],
        "correct_answer": "A",
        "explanation": "To enable personalization based on Azure AD group membership, `groupMembershipClaims` should be set to 'All'. To allow Azure AD users to log in, `oauth2Permissions` should be configured for delegated permissions (e.g., `user_impersonation` from the API or `User.Read` from Microsoft Graph)."
    },
    {
        "question": "You have an Azure Batch project that processes and converts files and stores the files in Azure storage. You are developing a function to start the batch job. You add the following parameters to the function. You must ensure that converted files are placed in the container referenced by the outputContainerSasUrl parameter. Files which fail to convert are places in the container referenced by the failedContainerSasUrl parameter. You need to ensure the files are correctly processed. How should you complete the code segment?",
        "options": [
            "A. Box 1: CreateJob, Box 2: TaskSuccess, Box 3: TaskFailure, Box 4: OutputFiles",
            "B. Box 1: AddTask, Box 2: TaskCompletion, Box 3: TaskSuccess, Box 4: InputFiles",
            "C. Box 1: SubmitJob, Box 2: TaskFailure, Box 3: TaskCompletion, Box 4: ResourceFiles",
            "D. Box 1: RunJob, Box 2: TaskSuccess, Box 3: TaskCompletion, Box 4: EnvironmentSettings"
        ],
        "correct_answer": "A",
        "explanation": "When configuring output files for Azure Batch tasks, you define `OutputFiles` that specify where files should be uploaded. `TaskSuccess` condition ensures upload on successful task exit (exit code 0), and `TaskFailure` handles uploads on non-zero exit codes for failed tasks. `CreateJob` is used to create the job."
    },
    {
        "question": "You develop a software as a service (SaaS) offering to manage photographs. Users upload photos to a web service which then stores the photos in Azure Storage Blob storage. The storage account type is General-purpose V2. When photos are uploaded, they must be processed to produce and save a mobile-friendly version of the image. The process to produce a mobile-friendly version of the image must start in less than one minute. You need to design the process that starts the photo processing. Solution: Move photo processing to an Azure Function triggered from the blob upload. Does the solution meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "correct_answer": "A",
        "explanation": "Triggering an Azure Function directly from a blob upload event is an efficient, serverless way to process data (like images) in near real-time, meeting the requirement for processing to start in less than one minute, especially with General-purpose V2 storage accounts that support Event Grid integration."
    },
    {
        "question": "Contoso, Ltd. provides an API to customers by using Azure API Management (APIM). The API authorizes users with a JWT token. You must implement response caching for the APIM gateway. The caching mechanism must detect the user ID of the client that accesses data for a given location and cache the response for that user ID. You need to add the following policies to the policies file: • a set-variable policy to store the detected user identity • a cache-lookup-value policy • a cache-store-value policy • a find-and-replace policy to update the response body with the user profile information To which policy section should you add the policies?",
        "options": [
            "A. set-variable: Inbound, cache-lookup-value: Inbound, cache-store-value: Outbound, find-and-replace: Outbound",
            "B. set-variable: Outbound, cache-lookup-value: Outbound, cache-store-value: Inbound, find-and-replace: Inbound",
            "C. set-variable: Inbound, cache-lookup-value: Outbound, cache-store-value: Inbound, find-and-replace: Outbound",
            "D. set-variable: Outbound, cache-lookup-value: Inbound, cache-store-value: Outbound, find-and-replace: Inbound"
        ],
        "correct_answer": "A",
        "explanation": "Policy sections in API Management determine when policies are applied. `set-variable` and `cache-lookup-value` policies typically operate on incoming requests (Inbound). `cache-store-value` and `find-and-replace` policies modify the response before sending it back (Outbound)."
    },
    {
        "question": "You have a web service that is used to pay for food deliveries. The web service uses Azure Cosmos DB as the data store. You plan to add a new feature that allows users to set a tip amount. The new feature requires that a property named tip on the document in Cosmos DB must be present and contain a numeric value. There are many existing websites and mobile apps that use the web service that will not be updated to set the tip property for some time. How should you complete the trigger?",
        "options": [
            "A. Box 1: getContext().getRequest(), Box 2: if(isNaN(i)[\"tip\"] ..), Box 3: r.setBody(i);",
            "B. Box 1: value(), Box 2: if (typeof i[\"tip\"] == 'number'), Box 3: r.setValue(i);",
            "C. Box 1: _readDocument('item'), Box 2: if (request.getValue('tip') == null), Box 3: _replaceDocument(i);",
            "D. Box 1: getContext().getResponse(), Box 2: if (i['tip'] != null), Box 3: _upsertDocument(i);"
        ],
        "correct_answer": "A",
        "explanation": "To validate and ensure a numeric 'tip' property is present in a Cosmos DB document via a pre-trigger: use `getContext().getRequest()` to get the request body, validate `tip` using `isNaN()`, and update the request body with `r.setBody(i)`."
    },
    {
        "question": "You have an app that stores player scores for an online game. The app stores data in Azure tables using a class named PlayerScore as the table entity. The table is populated with 100,000 records. You are reviewing the following section of code that is intended to retrieve 20 records where the player score exceeds 15,000. For each of the following statements, select Yes if the statement is true. Otherwise, select No.",
        "options": [
            "A. The code queries the Azure table and retrieves the TimePlayed property from the table: No. The code will display a maximum of twenty records: Yes. All records will be sent to the client. The client will display records for scores greater than or equal to 15,000: Yes. The scoreItem key property of the KeyValuePairs that ExecuteQuery returns will contain a value for PlayerID: Yes.",
            "B. The code queries the Azure table and retrieves the TimePlayed property from the table: Yes. The code will display a maximum of twenty records: No. All records will be sent to the client. The client will display records for scores greater than or equal to 15,000: No. The scoreItem key property of the KeyValuePairs that ExecuteQuery returns will contain a value for PlayerID: No.",
            "C. The code queries the Azure table and retrieves the TimePlayed property from the table: No. The code will display a maximum of twenty records: No. All records will be sent to the client. The client will display records for scores greater than or equal to 15,000: Yes. The scoreItem key property of the KeyValuePairs that ExecuteQuery returns will contain a value for PlayerID: No.",
            "D. The code queries the Azure table and retrieves the TimePlayed property from the table: Yes. The code will display a maximum of twenty records: Yes. All records will be sent to the client. The client will display records for scores greater than or equal to 15,000: No. The scoreItem key property of the KeyValuePairs that ExecuteQuery returns will contain a value for PlayerID: Yes."
        ],
        "correct_answer": "A",
        "explanation": "The `TableQuery.Take(20)` method limits the results to 20. Filtering is applied server-side. Key properties in query results will include PlayerID if it's part of the entity's keys."
    },
    {
        "question": "You use Azure Table storage to store customer information for an application. The data contains customer details and is partitioned by last name. You need to create a query that returns all customers with the last name Smith. Which code segment should you use?",
        "options": [
            "A. TableQuery.Generate FilterCondition(\"PartitionKey\", Equals, \"Smith\")",
            "B. TableQuery. Generate FilterCondition(\"LastName\", Equals, \"Smith\")",
            "C. TableQuery.Generate FilterCondition(\"PartitionKey\", Query Comparisons. Equal, \"Smith\")",
            "D. TableQuery Generate FilterCondition(\"LastName\", QueryComparisons. Equal, \"Smith\")"
        ],
        "correct_answer": "C",
        "explanation": "To retrieve all entities in a partition with PartitionKey=\"Smith\", the correct code segment is 'TableQuery.Generate FilterCondition(\"PartitionKey\", QueryComparisons. Equal, \"Smith\")'."
    },
    {
        "question": "You are developing a project management service by using ASP.NET. The service hosts conversations, files, to-do lists, and a calendar that users can interact with at any time. The application uses Azure Search for allowing users to search for keywords in the project data. You need to implement code that creates the object which is used to create indexes in the Azure Search service. Which object(s) should you use?",
        "options": [
            "A. Search Service",
            "B. SearchIndexClient",
            "C. SearchServiceClient",
            "D. SearchCredentials",
            "E. B and C"
        ],
        "correct_answer": "E",
        "explanation": "The client libraries for Azure Search define classes like SearchServiceClient and SearchIndexClient for operations related to the search service and indexes respectively. Both are used for creating and managing indexes."
    },
    {
        "question": "You are developing a solution that will use Azure messaging services. You need to ensure that the solution uses a publish-subscribe model and eliminates the need for constant polling. What are two possible ways to achieve the goal?",
        "options": [
            "A. Service Bus",
            "B. Event Hub",
            "C. Event Grid",
            "D. Queue",
            "E. A and C"
        ],
        "correct_answer": "E",
        "explanation": "For a publish-subscribe model that eliminates constant polling, Azure Service Bus and Azure Event Grid are recommended. Service Bus is suitable for high-value enterprise messaging, while Event Grid provides event-driven architecture for reacting to state changes."
    },
    {
        "question": "You develop a serverless application using several Azure Functions. These functions connect to data from within the code. You want to configure tracing for an Azure Function App project. You need to change configuration settings in the host.json file. Which tool should you use?",
        "options": [
            "A. Azure portal",
            "B. Azure PowerShell",
            "C. Azure Functions Core Tools (Azure CLI)",
            "D. Visual Studio"
        ],
        "correct_answer": "A",
        "explanation": "The host.json file, which contains runtime-specific configurations for an Azure Function App, can be directly updated using the function editor built into the Azure portal."
    },
    {
        "question": "You are writing code to create and run an Azure Batch job. You have created a pool of compute nodes. You need to choose the right class and its method to submit a batch job to the Batch service. Which method should you use?",
        "options": [
            "A. JobOperations.CreateJob()",
            "B. CloudJob.Enable (IEnumerable<BatchClientBehavior>)",
            "C. CloudJob.CommitAsync(IEnumerable<BatchClientBehavior>, CancellationToken)",
            "D. JobOperations.EnableJob(String, IEnumerable<BatchClientBehavior>)",
            "E. JobOperations. Enable JobAsync(Strin)",
            "F. IEnumerable<BatchClientBehavior>. CancellationToken)"
        ],
        "correct_answer": "C",
        "explanation": "After creating a `CloudJob` object using `BatchClient.JobOperations.CreateJob`, the `Commit` method (or `CommitAsync` for asynchronous operations) is used to submit the job to the Batch service."
    },
    {
        "question": "You develop Azure solutions. You must connect to a No-SQL globally-distributed database by using the .NET API. You need to create an object to configure and execute requests in the database. Which code segment should you use?",
        "options": [
            "A. new Container(EndpointUri, PrimaryKey);",
            "B. new Database(Endpoint, PrimaryKey);",
            "C. new CosmosClient(EndpointUri, PrimaryKey);"
        ],
        "correct_answer": "C",
        "explanation": "To connect to an Azure Cosmos DB (No-SQL globally-distributed database) using the .NET API and create an object for configuring and executing requests, you should use the `CosmosClient` class. Example: `new CosmosClient(EndpointUri, PrimaryKey)`."
    },
    {
        "question": "You are developing an Azure Cosmos DB solution by using the Azure Cosmos DB SQL API. The data includes millions of documents. Each document may contain hundreds of properties. The properties of the documents do not contain distinct values for partitioning. Azure Cosmos DB must scale individual containers in the database to meet the performance needs of the application by spreading the workload evenly across all partitions over time. You need to select a partition key. Which two partition keys can you use?",
        "options": [
            "A. a concatenation of multiple property values with a random suffix appended",
            "B. a single property value that does not appear frequently in the documents",
            "C. a hash suffix appended to a property value",
            "D. a value containing the collection name",
            "E. A and C"
        ],
        "correct_answer": "E",
        "explanation": "To ensure even workload distribution across partitions in Azure Cosmos DB when distinct values are not naturally present, you can use synthetic partition keys formed by concatenating multiple property values or by appending a random or hash suffix to a property value. This allows for parallel write operations across partitions."
    },
    {
        "question": "A company is developing a solution that allows smart refrigerators to send temperature information to a central location. You have an existing Service Bus. The solution must receive and store messages until they can be processed. You create an Azure Service Bus instance by providing a name, pricing tier, subscription, resource group, and location. You need to complete the configuration. Which Azure CLI or PowerShell command should you run?",
        "options": [
            "A. az servicebus namespace create -resource-group fridge-rg -name fridge-ns -location fridge-loc",
            "B. az servicebus queue create --resource-group fridge-rg --namespace-name fridge-ns --name fridge-q",
            "C. connectionString=\$(az servicebus namespace authorization-rule keys list --resource-group fridge-rg --fridge-ns fridge-ns --name RootManageSharedAccessKey --query primaryConnectionString --output tsv)",
            "D. az group create --name fridge -rg --location fridge-log"
        ],
        "correct_answer": "B",
        "explanation": "Since a Service Bus instance (namespace) has already been created, the next step to enable message reception and storage is to create a Service Bus queue within that namespace. The command `az servicebus queue create` is used for this purpose."
    },
    {
        "question": "You are developing an ASP.NET Core Web API web service. The web service uses Azure Application Insights for all telemetry and dependency tracking. The web service reads and writes data to a database other than Microsoft SQL Server. You need to ensure that dependency tracking works for calls to the third-party database. Which two Dependency Telemetry properties should you store in the database?",
        "options": [
            "A. Telemetry.Context. Operation.Id",
            "B. Tetemetry. Context.Cloud.RoleInstance",
            "C. Telemetry.Id",
            "D. Telemetry.ContextSession.Id",
            "E. Telemetry.Name",
            "F. A and C"
        ],
        "correct_answer": "F",
        "explanation": "For custom operations tracking and ensuring dependency tracking works for calls to third-party databases with Application Insights, `Telemetry.Context.Operation.Id` and `Telemetry.Id` are typically used to correlate operations and dependencies."
    },
    {
        "question": "You develop and deploy a Java RESTful API to Azure App Service. You open a browser and navigate to the URL for the API. You receive the following error message: Failed to load http://api: No 'Access- Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost: 6000' is therefore not allowed access You need to resolve the error. What should you do?",
        "options": [
            "A. Bind an SSL certificate",
            "B. Enable authentication",
            "C. Enable CORS",
            "D. Map a custom domain",
            "E. Add a CDN"
        ],
        "correct_answer": "C",
        "explanation": "The 'Access-Control-Allow-Origin' header missing error indicates a Cross-Origin Resource Sharing (CORS) issue. To resolve this, you need to enable CORS for your API in Azure App Service, allowing requests from specified origins."
    }
]

# Initialize Streamlit session state variables
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = None
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

st.set_page_config(layout="centered", page_title="Azure AZ-204 Quiz")

st.title("Azure AZ-204 Exam Prep Quiz")
st.markdown("Test your knowledge on Azure Development Solutions!")

if st.session_state.quiz_finished:
    st.header("Quiz Completed!")
    st.write(f"Your final score: {st.session_state.score} out of {len(quiz_questions)}")
    if st.button("Restart Quiz"):
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.session_state.user_answer = None
        st.session_state.quiz_finished = False
        st.experimental_rerun()
else:
    # Display current question
    current_question = quiz_questions[st.session_state.current_question_index]
    st.subheader(f"Question {st.session_state.current_question_index + 1}/{len(quiz_questions)}")
    st.write(current_question["question"])

    # Display options
    # Use st.radio for single-choice selection
    selected_option = st.radio(
        "Choose your answer:",
        options=current_question["options"],
        key=f"question_{st.session_state.current_question_index}",
        disabled=st.session_state.show_feedback # Disable radio buttons after submission
    )

    # Check answer button
    if st.button("Submit Answer", disabled=st.session_state.show_feedback):
        st.session_state.user_answer = selected_option
        st.session_state.show_feedback = True
        # Determine if the answer is correct
        # Get the letter of the selected option (e.g., "A. Option Text" -> "A")
        selected_answer_letter = st.session_state.user_answer.split('.')[0]
        if selected_answer_letter == current_question["correct_answer"]:
            st.session_state.score += 1

        st.experimental_rerun() # Rerun to show feedback and disable buttons

    # Display feedback if submitted
    if st.session_state.show_feedback:
        selected_answer_letter = st.session_state.user_answer.split('.')[0]
        if selected_answer_letter == current_question["correct_answer"]:
            st.success(f"Correct! Your score: {st.session_state.score}")
        else:
            st.error(f"Incorrect. The correct answer was {current_question['correct_answer']}. Your score: {st.session_state.score}")
        st.info(f"Explanation: {current_question['explanation']}")

        # Next question button
        if st.button("Next Question"):
            st.session_state.current_question_index += 1
            st.session_state.show_feedback = False
            st.session_state.user_answer = None
            if st.session_state.current_question_index >= len(quiz_questions):
                st.session_state.quiz_finished = True
            st.experimental_rerun()