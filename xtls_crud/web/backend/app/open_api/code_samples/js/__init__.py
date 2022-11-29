from ..models import CodeSample
from ....core.settings import settings

inbound__get__js__sample = CodeSample(
    lang="JavaScript",
    source=f"""
const axios = require('axios');
    
const options = {{
    method: 'GET',
    url: '{settings.SERVER_HOST}/api/v1/inbounds/',
    headers: {{}}
}};
    
axios.request(options).then(function (response) {{
    console.log(response.data);
}}).catch(function (error) {{
    console.error(error);
}});
""",
    label="JavaScript"
)

inbound__post__js__sample = CodeSample(
    lang="JavaScript",
    source=f"""
const axios = require('axios');

const options = {{
    method: 'POST',
    url: '{settings.SERVER_HOST}/api/v1/inbounds/',
    headers: {{
        'Content-Type': 'application/json'
    }},
    data: {{
        "user_id": 1,
        "up": "100GB",
        "down": 107374182400,
        "total": 0,
        "remark": "amiwrpremium",
        "enable": true,
        "expiry_time": "1MO",
        "listen": "as",
        "port": 443,
        "protocol": "vmess",
        "uuid": "f80365b4-ef07-4d39-a938-5275dc5db89e",
        "network": "ws",
        "security": "tls",
        "server_name": "http://127.0.0.1/",
        "ws_path": "/alTdjZ",
        "tag": 1,
        "sniffing": true
    }}
}};

axios.request(options).then(function (response) {{
    console.log(response.data);
}}).catch(function (error) {{
    console.error(error);
}});
""",
    label="JavaScript"
)

builders__post__js__sample = CodeSample(
    lang="JavaScript",
    source=f"""
const axios = require('axios');

const options = {{
    method: 'POST',
    url: '{settings.SERVER_HOST}/api/v1/builders/',
    headers: {{'Content-Type': 'application/json'}},
    data: {{
        "user_id": 1,
        "up": "100GB",
        "down": 107374182400,
        "total": 0,
        "remark": "amiwrpremium",
        "enable": True,
        "expiry_time": "1MO",
        "listen": "listen",
        "port": 443,
        "protocol": "vmess",
        "uuid": "d36b31f0-44de-4576-a254-27d1d9410997",
        "network": "ws",
        "security": "tls",
        "server_name": "{settings.SERVER_HOST}",
        "ws_path": "/owzvHG",
        "tag": 1,
        "sniffing": true
    }}
}};

axios.request(options).then(function (response) {{
    console.log(response.data);
}}).catch(function (error) {{
    console.error(error);
}});
""",
    label="JavaScript"
)
