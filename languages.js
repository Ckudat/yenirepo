const languages = [
    {"id": 1, "name": "Turkish", "iso_code": "TR"},
    {"id": 5, "name": "English", "iso_code": "EN"}
];
const listItems = languages.map(language =>
    <li key={language.id}>
        {language.name}
    </li>
);

return (
    <ul>{listItems}</ul>
);
