int main() {
  int n, t, a, c, d;
  c = 0;
  d = 0;
  scanf("%d %d", &n, &t);
  while (c < t) {
    scanf("%d", &a);
    c += 86400 - a;
    d++;
  }
  printf("%d", d);
  return 0;
}