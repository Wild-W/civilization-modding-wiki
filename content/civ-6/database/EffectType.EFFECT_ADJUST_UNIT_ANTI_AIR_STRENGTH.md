---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ANTI_AIR_STRENGTH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ANTI_AIR_STRENGTH
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GDR_AA_DEFENSE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GDR_AA_DEFENSE",
		"MODIFIER_SINGLE_UNIT_ADJUST_ANTI_AIR_STRENGTH_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GDR_AA_DEFENSE",
		"Amount",
		40
	);
	
```

