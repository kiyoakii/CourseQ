from app.libs.enums import UserTypeEnum
from app.libs.error_code import DeleteSuccess, Success
from app.libs.redprint import Redprint
from app.libs.token_auth import login_required, role_required, enroll_required
from app.models import Announce
from app.models.base import db
from app.validators.forms import AnnounceForm

api = Redprint('announce')


@api.route('/<int:pk>', methods=['DELETE'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Announce)
def delete_announce(pk):
    announce = Announce.query.get_or_404(pk)
    with db.auto_commit():
        db.session.delete(announce)
    return DeleteSuccess()


@api.route('/<int:pk>', methods=['PUT'])
@role_required(UserTypeEnum.TEACHER)
@enroll_required(Announce)
def update_announce(pk):
    announce = Announce.query.get_or_404(pk)
    form = AnnounceForm().validate_for_api()
    with db.auto_commit():
        form.populate_obj(announce)
    return Success()
