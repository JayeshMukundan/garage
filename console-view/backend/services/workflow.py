from db.orm import dbInterface
from utils.class_utils import get_class_for_name


class WorkflowService():

    def get_authorized_columns_to_pull(self, user_id, cls_name):
        cls = get_class_for_name(cls_name)
        # For now, return everything
        return cls.__table__.columns.keys()

    def get_object_by_id(self, user_id, cls_name, id):
        authorized_columns = self.get_authorized_columns_to_pull(user_id, cls_name)
        if not authorized_columns:
            raise Exception("User {} isn't authorized to pull the class {}".format(user_id, cls_name))

        row = dbInterface.get_by_id(cls_name, id)
        if not row:
            raise Exception("Object with id = {} doesn't exist for class {}".format(id, cls_name))

        columns = row.__table__.columns.keys()
        response = {}
        for col in columns:
            if col in authorized_columns:
                response[col] = getattr(row, col)
            else:
                response[col] = 'Not Authorized'
        return response


workflowService = WorkflowService()
