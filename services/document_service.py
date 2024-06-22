from models import db
from models.document import Document

class DocumentService:
    @staticmethod
    def get_all_documents():
        return Document.query.all()

    @staticmethod
    def get_document_by_id(doc_id):
        return Document.query.get(doc_id)

    @staticmethod
    def create_document(data):
        document = Document(**data)
        db.session.add(document)
        db.session.commit()
        return document

    @staticmethod
    def update_document(doc_id, data):
        document = Document.query.get(doc_id)
        if document:
            for key, value in data.items():
                setattr(document, key, value)
            db.session.commit()
        return document

    @staticmethod
    def delete_document(doc_id):
        document = Document.query.get(doc_id)
        if document:
            db.session.delete(document)
            db.session.commit()
        return document
