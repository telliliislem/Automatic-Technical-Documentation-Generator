public class SubscriptionAdminClient {
    /**
     * Deletes a snapshot.
     *
     * @param snapshot the name of the snapshot to delete.
     */
    public final void deleteSnapshot(ProjectSnapshotName snapshot) {
        DeleteSnapshotRequest request = DeleteSnapshotRequest.newBuilder()
               .setSnapshot(snapshot == null? null : snapshot.toString())
               .build();
        deleteSnapshot(request);
    }

    /**
     * Deletes a snapshot.
     *
     * @param snapshot the name of the snapshot to delete.
     */
    public final void deleteSnapshot(String snapshot) {
        DeleteSnapshotRequest request = DeleteSnapshotRequest.newBuilder()
               .setSnapshot(snapshot)
               .build();
        deleteSnapshot(request);
    }

    /**
     * Creates a new subscription.
     *
     * @param name the name of the subscription to create.
     * @param topic the name of the topic from which this subscription is receiving messages.
     * @param pushConfig the configuration for a push subscription.
     * @param ackDeadlineSeconds the maximum number of seconds that the server will retain a message.
     * @return the created subscription.
     */
    public final Subscription createSubscription(
            ProjectSubscriptionName name,
            ProjectTopicName topic,
            PushConfig pushConfig,
            int ackDeadlineSeconds) {
        Subscription request = Subscription.newBuilder()
               .setName(name == null? null : name.toString())
               .setTopic(topic == null? null : topic.toString())
               .setPushConfig(pushConfig)
               .setAckDeadlineSeconds(ackDeadlineSeconds)
               .build();
        return createSubscription(request);
    }

    /**
     * Creates a new subscription.
     *
     * @param name the name of the subscription to create.
     * @param topic the name of the topic from which this subscription is receiving messages.
     * @param pushConfig the configuration for a push subscription.
     * @param ackDeadlineSeconds the maximum number of seconds that the server will retain a message.
     * @return the created subscription.
     */
    public final Subscription createSubscription(
            String name, String topic, PushConfig pushConfig, int ackDeadlineSeconds) {
        Subscription request = Subscription.newBuilder()
               .setName(name)
               .setTopic(topic)
               .setPushConfig(pushConfig)
               .setAckDeadlineSeconds(ackDeadlineSeconds)
               .build();
        return createSubscription(request);
    }

    /**
     * Gets a subscription.
     *
     * @param subscription the name of the subscription to get.
     * @return the subscription.
     */
    public final Subscription getSubscription(ProjectSubscriptionName subscription) {
        GetSubscriptionRequest request = GetSubscriptionRequest.newBuilder()
               .setSubscription(subscription == null? null : subscription.toString())
               .build();
        return getSubscription(request);
    }

    /**
     * Gets a subscription.
     *
     * @param subscription the name of the subscription to get.
     * @return the subscription.
     */
    public final Subscription getSubscription(String subscription) {
        GetSubscriptionRequest request = GetSubscriptionRequest.newBuilder()
               .setSubscription(subscription)
               .build();
        return getSubscription(request);
    }

    /**
     * Lists all subscriptions for a given project.
     *
     * @param project the name of the project to list subscriptions for.
     * @return a paged response containing the subscriptions.
     */
    public final ListSubscriptionsPagedResponse listSubscriptions(ProjectName project) {
        ListSubscriptionsRequest request = ListSubscriptionsRequest.newBuilder()
               .setProject(project == null? null : project.toString())
               .build();
        return listSubscriptions(request);
    }

    /**
     * Lists all subscriptions for a given project.
     *
     * @param project the name of the project to list subscriptions for.
     * @return a paged response containing the subscriptions.
     */
    public final ListSubscriptionsPagedResponse listSubscriptions(String project) {
        ListSubscriptionsRequest request = ListSubscriptionsRequest.newBuilder()
               .setProject(project)
               .build();
        return listSubscriptions(request);
    }

    /**
     * Deletes a subscription.
     *
     * @param subscription the name of the subscription to delete.
     */
    public final void deleteSubscription(ProjectSubscriptionName subscription) {
        DeleteSubscriptionRequest request = DeleteSubscriptionRequest.newBuilder()
               .setSubscription(subscription == null? null : subscription.toString())
               .build();
        deleteSubscription(request);
    }

    /**
     * Deletes a subscription.
     *
     * @param subscription the name of the subscription to delete.
     */
    public final void deleteSubscription(String subscription) {
        DeleteSubscriptionRequest request = DeleteSubscriptionRequest.newBuilder()
               .setSubscription(subscription)
               .build();
        deleteSubscription(request);
    }

    /**
     * Modifies the push configuration for a subscription.
     *
     * @param subscription the name of the subscription to modify.
     * @param pushConfig the new push configuration.
     */
    public final void modifyPushConfig(ProjectSubscriptionName subscription, PushConfig pushConfig) {
        ModifyPushConfigRequest request = ModifyPushConfigRequest.newBuilder()
               .setSubscription(subscription == null? null : subscription.toString())
               .setPushConfig(pushConfig)
               .build();
        modifyPushConfig(request);
    }

    /**
     * Modifies the push configuration for a subscription.
     *
     * @param subscription the name of the subscription to modify.
     * @param pushConfig the new push configuration.
     */
    public final void modifyPushConfig(String subscription, PushConfig pushConfig) {
        ModifyPushConfigRequest request = ModifyPushConfigRequest.newBuilder()
                               .setSubscription(subscription)
                .setPushConfig(pushConfig)
                .build();
        modifyPushConfig(request);
    }
    