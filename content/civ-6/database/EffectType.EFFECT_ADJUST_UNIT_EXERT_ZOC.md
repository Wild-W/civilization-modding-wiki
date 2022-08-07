---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_EXERT_ZOC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_EXERT_ZOC
>
> * Class: `UNITS`
> * Parameters:
>	* Exert `Boolean`

## Samples

```SQL {title="SUPPRESSION_BONUS_EXERT_ZOC"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SUPPRESSION_BONUS_EXERT_ZOC",
		"MODIFIER_PLAYER_UNIT_ADJUST_EXERT_ZOC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SUPPRESSION_BONUS_EXERT_ZOC",
		"Exert",
		1
	);
	
```

