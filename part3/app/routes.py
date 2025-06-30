@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated = facade.update_user(user_id, data)
    return jsonify({
        'id': updated.id,
        'email': updated.email
    })

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    facade.delete_user(user_id)
    return jsonify({'status': 'deleted'}), 204
