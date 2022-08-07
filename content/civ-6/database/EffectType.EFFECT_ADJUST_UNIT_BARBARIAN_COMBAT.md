---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_BARBARIAN_COMBAT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_BARBARIAN_COMBAT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="DISCIPLINE_BARBARIANCOMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DISCIPLINE_BARBARIANCOMBAT",
		"MODIFIER_PLAYER_UNITS_ADJUST_BARBARIAN_COMBAT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DISCIPLINE_BARBARIANCOMBAT",
		"Amount",
		5
	);
	
```

