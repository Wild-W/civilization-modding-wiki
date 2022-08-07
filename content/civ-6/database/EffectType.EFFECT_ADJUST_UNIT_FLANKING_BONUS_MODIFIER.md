---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_FLANKING_BONUS_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_FLANKING_BONUS_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Percent `Integer`

## Samples

```SQL {title="HORATIO_NELSON_FLANKING_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HORATIO_NELSON_FLANKING_BONUS",
		"MODIFIER_PLAYER_UNIT_ADJUST_FLANKING_BONUS_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HORATIO_NELSON_FLANKING_BONUS",
		"Percent",
		50
	);
	
```

