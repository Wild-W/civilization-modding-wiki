---
tags:
- EffectType
title: EFFECT_REPLACE_PLAYER_GOVERNMENT_SLOT_TYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_REPLACE_PLAYER_GOVERNMENT_SLOT_TYPE
>
> * Class: `PLAYERS`
> * Parameters:
>	* AddedGovernmentSlotType `String`
>		* [GovernmentSlots.GovernmentSlotType]
>	* ReplacedGovernmentSlotType `String`
>		* [GovernmentSlots.GovernmentSlotType]
>	* ReplacesAll `Boolean`

## Samples
```SQL {title="TRAIT_REPLACE_MILITARY_SLOT_WITH_WILDCARD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_REPLACE_MILITARY_SLOT_WITH_WILDCARD",
		"MODIFIER_PLAYER_CULTURE_REPLACE_GOVERNMENT_SLOTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_REPLACE_MILITARY_SLOT_WITH_WILDCARD",
		"AddedGovernmentSlotType",
		"SLOT_WILDCARD"
	),
	(
		"TRAIT_REPLACE_MILITARY_SLOT_WITH_WILDCARD",
		"ReplacedGovernmentSlotType",
		"SLOT_MILITARY"
	);
	
```

```SQL {title="TRAIT_ALL_DIPLO_POLICY_ARE_WILDCARDS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ALL_DIPLO_POLICY_ARE_WILDCARDS",
		"MODIFIER_PLAYER_CULTURE_REPLACE_GOVERNMENT_SLOTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ALL_DIPLO_POLICY_ARE_WILDCARDS",
		"AddedGovernmentSlotType",
		"SLOT_WILDCARD"
	),
	(
		"TRAIT_ALL_DIPLO_POLICY_ARE_WILDCARDS",
		"ReplacedGovernmentSlotType",
		"SLOT_DIPLOMATIC"
	),
	(
		"TRAIT_ALL_DIPLO_POLICY_ARE_WILDCARDS",
		"ReplacesAll",
		1
	);
	
```

