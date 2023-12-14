import aws_cdk as core
import aws_cdk.assertions as assertions

from supervised_learning_agile.supervised_learning_agile_stack import SupervisedLearningAgileStack

# example tests. To run these tests, uncomment this file along with the example
# resource in supervised_learning_agile/supervised_learning_agile_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SupervisedLearningAgileStack(app, "supervised-learning-agile")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
