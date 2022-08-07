---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_VALID_IMPROVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_VALID_IMPROVEMENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]

## Samples
```SQL {title="MINOR_CIV_LA_VENTA_CAN_COLLOSSAL_HEAD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_LA_VENTA_CAN_COLLOSSAL_HEAD",
		"MODIFIER_PLAYER_ADJUST_VALID_IMPROVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_LA_VENTA_CAN_COLLOSSAL_HEAD",
		"ImprovementType",
		"IMPROVEMENT_COLOSSAL_HEAD"
	);
	
```

