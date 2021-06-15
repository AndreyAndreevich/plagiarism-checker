# plagiarism-checker action

Проверяет текст на плагиат на text.ru

## Inputs
* `user_key` - user_key аккаунта text.ru
* `files` - список файлов через зяпятую
* `public` - доступен ли результат всем (default: false)
* `min_uniq`- минимальный процент уникальности (default: 0)

## Outputs
* `results` - список результатов проверок
Пример:
```json
{
    "__test__/test1.md": {"uniq": 0.0, "url": "https://text.ru/antiplagiat/60c7cc2d2ef9b"}, 
    "__test__/test2.md": {"uniq": 100.0, "url": "https://text.ru/antiplagiat/60c7cc2e17df3"}
}
```

## Example usage
```yaml
uses: AndreyAndreevich/plagiarism-checker@v1
id: plagiarism
with:
  user_key: ${{ secrets.USER_KEY }}
  files: ${{ env.files }}
  public: 'true'
  min_uniq: '10'
```
