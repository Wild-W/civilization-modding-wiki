---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ATTACK_EXPERIENCE_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ATTACK_EXPERIENCE_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MINOR_CIV_KABUL_UNIT_EXPERIENCE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_KABUL_UNIT_EXPERIENCE_BONUS",
		"MODIFIER_PLAYER_UNITS_ADJUST_UNIT_ATTACK_EXPERIENCE_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_KABUL_UNIT_EXPERIENCE_BONUS",
		"Amount",
		100
	);
	
```

