---
tags:
- EffectType
title: EFFECT_DISTRICT_ADD_NAVAL_UNIT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DISTRICT_ADD_NAVAL_UNIT
>
> * Class: `PLAYERS`
> * Parameters:
>	* DistrictType `String`

## Samples
```SQL {title="TRAIT_ROYAL_NAVY_DOCKYARD_NAVAL_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ROYAL_NAVY_DOCKYARD_NAVAL_UNIT",
		"MODIFIER_PLAYER_ADJUST_DISTRICT_ADD_NAVAL_UNIT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ROYAL_NAVY_DOCKYARD_NAVAL_UNIT",
		"DistrictType",
		"DISTRICT_ROYAL_NAVY_DOCKYARD"
	);
	
```

