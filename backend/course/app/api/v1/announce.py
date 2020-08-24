from app.libs.error_code import DeleteSuccess, Success
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required
from app.models import Announce
from app.models.base import db
from app.validators.forms import AnnounceForm

api = Redprint('announce')


@login_required
@api.route('/<int:pk>', methods=['DELETE'])
def delete_announce(pk):
    announce = Announce.query.get_or_404(pk)
    with db.auto_commit():
        db.session.delete(announce)
    return DeleteSuccess()


@login_required
@api.route('/<int:pk>', methods=['PUT'])
def update_announce(pk):
    announce = Announce.query.get_or_404(pk)
    form = AnnounceForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(announce)
    return Success()
