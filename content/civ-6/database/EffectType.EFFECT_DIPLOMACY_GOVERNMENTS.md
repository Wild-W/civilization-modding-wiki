---
tags:
- EffectType
title: EFFECT_DIPLOMACY_GOVERNMENTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_GOVERNMENTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* IncrementTurns `Integer`
>	* IncrementValue `Integer`
>	* SimpleModifierDescription `String`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_GOVERNMENT_DIFFERENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_GOVERNMENT_DIFFERENT",
		"MODIFIER_PLAYER_DIPLOMACY_GOVERNMENTS",
		"PLAYER_HAS_DIFFERENT_GOVERNMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_GOVERNMENT_DIFFERENT",
		"IncrementTurns",
		1
	),
	(
		"STANDARD_DIPLOMATIC_GOVERNMENT_DIFFERENT",
		"IncrementValue",
		"-1"
	),
	(
		"STANDARD_DIPLOMATIC_GOVERNMENT_DIFFERENT",
		"SimpleModifierDescription",
		"LOC_TOOLTIP_SAMPLE_DIPLOMACY_GOVERNMENT_DIFFERENT"
	);
	
```

```SQL {title="STANDARD_DIPLOMATIC_GOVERNMENT_SAME"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_GOVERNMENT_SAME",
		"MODIFIER_PLAYER_DIPLOMACY_GOVERNMENTS",
		"PLAYER_HAS_SAME_GOVERNMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_GOVERNMENT_SAME",
		"SimpleModifierDescription",
		"LOC_TOOLTIP_SAMPLE_DIPLOMACY_GOVERNMENT_SAME"
	);
	
```

