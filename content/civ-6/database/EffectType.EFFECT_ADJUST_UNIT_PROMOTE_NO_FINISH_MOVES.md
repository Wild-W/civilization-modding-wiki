---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PROMOTE_NO_FINISH_MOVES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PROMOTE_NO_FINISH_MOVES
>
> * Class: `UNITS`
> * Parameters:
>	* NoFinishMoves `Boolean`
>		* [Units.UnitType]

## Samples

```SQL {title="TRAIT_PROMOTE_NO_FINISH_MOVES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_PROMOTE_NO_FINISH_MOVES",
		"MODIFIER_PLAYER_UNITS_PROMOTE_NO_FINISH_MOVES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_PROMOTE_NO_FINISH_MOVES",
		"NoFinishMoves",
		1
	);
	
```

