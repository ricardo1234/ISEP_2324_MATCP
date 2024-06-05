from PoissonExtension import PoissonExtension

mystats = PoissonExtension(mean=1)

#24.1
print(f"A probabilidade de x = 0 : {mystats.Equal(0):.3f}")
print(f"A probabilidade de x > 0 : {(mystats.Greater(0)):.3f}")

#24.2
print(f"A probabilidade de x <= 1 : {mystats.LessOrEqual(1):.3f}")
print(f"A probabilidade de x > 1 : {(mystats.Greater(1)):.3f}")

print(f"{mystats.HappeningAfterAnother(mystats.Greater(1), mystats.GreaterOrEqual(1)):.3f}")
