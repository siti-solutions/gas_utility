
# Application Paths

## 1. **Home Page**
- **URL**: `/`
- **Purpose**: Redirects to the login or dashboard depending on whether the user is authenticated.

## 2. **Create Service Request**
- **URL**: `/service/create/`
- **Purpose**: Allows customers to submit a new service request.

## 3. **Service Request Status**
- **URL**: `/service/status/<int:request_id>/`
- **Purpose**: Displays the status of the service request and allows for adding comments.

## 4. **Notifications**
- **URL**: `/service/notifications/`
- **Purpose**: Shows the list of unread notifications related to service requests.

## 5. **Admin Dashboard**
- **URL**: `/service/admin/dashboard/`
- **Purpose**: Displays the dashboard for admin/support representatives to view and manage service requests.

## 6. **Django Admin**
- **URL**: `/admin/`
- **Purpose**: Admin interface for managing users, accounts, service requests, notifications, and comments.

