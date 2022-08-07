---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_GOVERNMENT_SLOT_TYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_GOVERNMENT_SLOT_TYPE
>
> * Class: `PLAYERS`
> * Parameters:
>	* GovernmentSlotType `String`
>		* [GovernmentSlots.GovernmentSlotType]

## Samples
```SQL {title="ALHAMBRA_MILITARY_GOVERNMENT_SLOT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALHAMBRA_MILITARY_GOVERNMENT_SLOT",
		"MODIFIER_PLAYER_CULTURE_ADJUST_GOVERNMENT_SLOTS_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALHAMBRA_MILITARY_GOVERNMENT_SLOT",
		"GovernmentSlotType",
		"SLOT_MILITARY"
	);
	
```

