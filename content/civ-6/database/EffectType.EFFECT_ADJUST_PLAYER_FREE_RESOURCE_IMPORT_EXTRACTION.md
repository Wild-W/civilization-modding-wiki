---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FREE_RESOURCE_IMPORT_EXTRACTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FREE_RESOURCE_IMPORT_EXTRACTION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples
```SQL {title="MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_XP2"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_XP2",
		"MODIFIER_PLAYER_ADJUST_FREE_RESOURCE_IMPORT_EXTRACTION",
		"PLAYER_HAS_NO_IMPROVED_ALUMINUM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_XP2",
		"Amount",
		2
	),
	(
		"MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_XP2",
		"ResourceType",
		"RESOURCE_ALUMINUM"
	);
	
```

