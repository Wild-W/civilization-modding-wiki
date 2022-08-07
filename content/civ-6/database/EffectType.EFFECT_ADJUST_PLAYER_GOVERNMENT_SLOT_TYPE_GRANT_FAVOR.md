---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_GOVERNMENT_SLOT_TYPE_GRANT_FAVOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_GOVERNMENT_SLOT_TYPE_GRANT_FAVOR
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* GovernmentSlotType `String`
>		* [GovernmentSlots.GovernmentSlotType]

## Samples
```SQL {title="TRAIT_WILD_CARD_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_WILD_CARD_FAVOR",
		"MODIFIER_PLAYER_ADJUST_GOVERNMENT_SLOT_TYPE_GRANT_FAVOR"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_WILD_CARD_FAVOR",
		"Amount",
		1
	),
	(
		"TRAIT_WILD_CARD_FAVOR",
		"GovernmentSlotType",
		"SLOT_WILDCARD"
	);
	
```

